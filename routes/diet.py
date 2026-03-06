from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from extensions import db
from models.models import MealPlan
from engines.diet_engine import generate_meal_plan
import json

diet = Blueprint('diet', __name__, url_prefix='/diet')

ALLERGEN_MAP = {
    'gluten':  ['wheat', 'bread', 'pasta', 'roti', 'oats', 'semolina', 'maida'],
    'dairy':   ['milk', 'paneer', 'curd', 'cheese', 'butter', 'ghee', 'yogurt', 'cream'],
    'nuts':    ['almond', 'peanut', 'cashew', 'walnut', 'pistachio'],
    'egg':     ['egg'],
    'soy':     ['tofu', 'soya', 'soy'],
    'seafood': ['fish', 'prawn', 'shrimp', 'tuna', 'salmon'],
}

def get_user_allergies(user):
    """Return a list of allergen keys the user has set in their profile."""
    if not hasattr(user, 'allergies') or not user.allergies:
        return []
    return [a.strip().lower() for a in user.allergies.split(',') if a.strip()]

def tag_allergens(meal_name):
    """Tag which allergens a meal contains based on its name."""
    name_lower = meal_name.lower()
    return [a for a, kws in ALLERGEN_MAP.items() if any(k in name_lower for k in kws)]

def meal_contains_user_allergen(meal_name, user_allergies):
    """Return True if a meal contains any of the user's allergens."""
    if not user_allergies:
        return False
    meal_allergens = tag_allergens(meal_name)
    return any(a in meal_allergens for a in user_allergies)

def flag_allergen_warnings(plan_data, user_allergies):
    """
    Attach allergen info and a warning flag to each meal in the plan.
    Meals matching the user's allergies get flagged so the template can highlight them.
    """
    for day in plan_data.get('days', []):
        for slot in ['breakfast', 'lunch', 'dinner', 'snack']:
            meal = day.get(slot, {})
            if isinstance(meal, dict):
                meal['allergens']       = tag_allergens(meal.get('name', ''))
                meal['allergy_warning'] = meal_contains_user_allergen(
                    meal.get('name', ''), user_allergies
                )
    return plan_data


@diet.route('/')
@login_required
def index():
    plan = MealPlan.query.filter_by(user_id=current_user.id)\
                         .order_by(MealPlan.created_at.desc()).first()
    plan_data     = None
    user_allergies = get_user_allergies(current_user)

    if plan and plan.plan_json:
        raw = json.loads(plan.plan_json)
        plan_data = {
            'days':                raw.get('days') or raw.get('plan', []),
            'target_calories':     raw.get('target_calories', 0),
            'weekly_avg_calories': raw.get('weekly_avg_calories') or raw.get('avg_daily_calories', 0),
            'weekly_avg_carbon':   raw.get('weekly_avg_carbon')   or raw.get('avg_daily_carbon', 0),
            'bmr':                 raw.get('bmr', 0),
            'swap_suggestions':    raw.get('swap_suggestions', []),
        }
        plan_data = flag_allergen_warnings(plan_data, user_allergies)

    return render_template('diet/index.html',
                           plan=plan,
                           plan_data=plan_data,
                           user_allergies=user_allergies)


@diet.route('/regenerate')
@login_required
def regenerate():
    user_allergies = get_user_allergies(current_user)

    # Pass allergies into the engine so meals can be filtered/swapped there too
    raw = generate_meal_plan(current_user)

    plan_data = {
        'days':                raw.get('days') or raw.get('plan', []),
        'target_calories':     raw.get('target_calories', 0),
        'weekly_avg_calories': raw.get('weekly_avg_calories') or raw.get('avg_daily_calories', 0),
        'weekly_avg_carbon':   raw.get('weekly_avg_carbon')   or raw.get('avg_daily_carbon', 0),
        'bmr':                 raw.get('bmr', 0),
        'swap_suggestions':    raw.get('swap_suggestions', []),
    }

    # Flag allergen warnings before saving
    plan_data = flag_allergen_warnings(plan_data, user_allergies)

    existing = MealPlan.query.filter_by(user_id=current_user.id).first()
    if existing:
        existing.plan_json      = json.dumps(plan_data)
        existing.total_calories = plan_data['weekly_avg_calories']
        existing.carbon_score   = plan_data['weekly_avg_carbon']
    else:
        db.session.add(MealPlan(
            user_id        = current_user.id,
            plan_json      = json.dumps(plan_data),
            total_calories = plan_data['weekly_avg_calories'],
            carbon_score   = plan_data['weekly_avg_carbon'],
        ))
    db.session.commit()
    flash('New meal plan generated! 🥗', 'success')
    return redirect(url_for('diet.index'))


@diet.route('/edit-meal', methods=['POST'])
@login_required
def edit_meal():
    data      = request.get_json()
    day_idx   = int(data.get('day', 0))
    slot      = data.get('slot', '')
    meal_name = data.get('meal_name', '').strip()
    calories  = int(data.get('calories', 0))
    carbon    = float(data.get('carbon', 0.0))

    plan = MealPlan.query.filter_by(user_id=current_user.id)\
                         .order_by(MealPlan.created_at.desc()).first()
    if not plan:
        return jsonify({'ok': False, 'msg': 'No plan found'})

    plan_data      = json.loads(plan.plan_json)
    user_allergies = get_user_allergies(current_user)
    days           = plan_data.get('days', [])

    if 0 <= day_idx < len(days):
        new_meal = {
            'name': meal_name, 'calories': calories,
            'carbon': carbon, 'protein': 0, 'carbs': 0, 'fat': 0,
            'allergens':       tag_allergens(meal_name),
            'allergy_warning': meal_contains_user_allergen(meal_name, user_allergies),
        }
        days[day_idx][slot] = new_meal
        plan.plan_json = json.dumps(plan_data)
        db.session.commit()
        return jsonify({'ok': True, 'allergy_warning': new_meal['allergy_warning']})
    return jsonify({'ok': False, 'msg': 'Invalid day'})