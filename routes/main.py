from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from extensions import db
from models.user import User
from models.models import FoodListing, ProgressLog
from datetime import datetime, timedelta

main = Blueprint('main', __name__)

@main.route('/')
def index():
    total_listings = FoodListing.query.count()
    claimed        = FoodListing.query.filter_by(status='claimed').count()
    total_users    = User.query.count()
    stats = {
        'food_saved_kg':  claimed * 2,
        'meals_provided': claimed,
        'active_users':   total_users,
        'co2_saved':      round(claimed * 1.5, 1)
    }
    return render_template('index.html', stats=stats)


@main.route('/dashboard')
@login_required
def dashboard():
    from models.models import MealPlan, ExercisePlan
    import json

    meal_plan = MealPlan.query.filter_by(user_id=current_user.id).order_by(MealPlan.created_at.desc()).first()
    ex_plan   = ExercisePlan.query.filter_by(user_id=current_user.id).order_by(ExercisePlan.created_at.desc()).first()
    today_log = ProgressLog.query.filter_by(user_id=current_user.id, log_date=datetime.utcnow().date()).first()

    week_logs = ProgressLog.query.filter(
        ProgressLog.user_id == current_user.id,
        ProgressLog.log_date >= (datetime.utcnow() - timedelta(days=7)).date()
    ).order_by(ProgressLog.log_date).all()

    streak    = sum(1 for l in week_logs if l.workout_done)
    meal_data = json.loads(meal_plan.plan_json) if meal_plan else None
    ex_data   = json.loads(ex_plan.plan_json)   if ex_plan   else None

    today_idx = datetime.utcnow().weekday()

    # Today's meal — handle both 'days' and legacy 'plan' key
    today_meal = None
    if meal_data:
        days = meal_data.get('days') or meal_data.get('plan', [])
        today_meal = days[today_idx] if today_idx < len(days) else None

    # Today's exercise — handle both 'plan' key formats
    today_ex = None
    if ex_data:
        ex_days = ex_data.get('plan', [])
        today_ex = ex_days[today_idx] if today_idx < len(ex_days) else None

    nearby_food = FoodListing.query.filter_by(status='available')\
                             .order_by(FoodListing.posted_at.desc()).limit(3).all()

    return render_template('dashboard.html',
        meal_plan   = meal_data,
        ex_plan     = ex_data,
        today_meal  = today_meal,
        today_ex    = today_ex,
        today_log   = today_log,
        week_logs   = week_logs,
        streak      = streak,
        nearby_food = nearby_food,
        now         = datetime.utcnow()
    )


@main.route('/profile/setup', methods=['GET', 'POST'])
@login_required
def setup_profile():
    if request.method == 'POST':
        current_user.age           = int(request.form.get('age', 25))
        current_user.weight        = float(request.form.get('weight', 70))
        current_user.height        = float(request.form.get('height', 170))
        current_user.gender        = request.form.get('gender', 'male')
        current_user.dietary_pref  = request.form.get('dietary_pref', 'veg')
        current_user.health_goal   = request.form.get('health_goal', 'stay_fit')
        current_user.fitness_level = request.form.get('fitness_level', 'beginner')
        current_user.equipment     = request.form.get('equipment', 'none')
        current_user.days_per_week = int(request.form.get('days_per_week', 4))
        current_user.location      = request.form.get('location', 'Hyderabad')
        current_user.profile_complete = True
        db.session.commit()

        from engines.diet_engine import generate_meal_plan
        from engines.exercise_engine import generate_exercise_plan
        from models.models import MealPlan, ExercisePlan
        import json

        raw_meal = generate_meal_plan(current_user)
        # Normalise meal plan keys
        meal_data = {
            'days':                raw_meal.get('days') or raw_meal.get('plan', []),
            'target_calories':     raw_meal.get('target_calories', 0),
            'weekly_avg_calories': raw_meal.get('weekly_avg_calories') or raw_meal.get('avg_daily_calories', 0),
            'weekly_avg_carbon':   raw_meal.get('weekly_avg_carbon')   or raw_meal.get('avg_daily_carbon', 0),
            'bmr':                 raw_meal.get('bmr', 0),
            'swap_suggestions':    raw_meal.get('swap_suggestions', []),
        }

        ex_data = generate_exercise_plan(current_user)

        mp = MealPlan(
            user_id        = current_user.id,
            plan_json      = json.dumps(meal_data),
            total_calories = meal_data['weekly_avg_calories'],
            carbon_score   = meal_data['weekly_avg_carbon']
        )
        db.session.add(mp)

        ep = ExercisePlan(
            user_id       = current_user.id,
            plan_json     = json.dumps(ex_data),
            fitness_goal  = current_user.health_goal,
            fitness_level = current_user.fitness_level,
            days_per_week = current_user.days_per_week
        )
        db.session.add(ep)
        db.session.commit()

        flash('Profile saved! Your personalized plans are ready. 🎉', 'success')
        return redirect(url_for('main.dashboard'))

    return render_template('profile_setup.html')


@main.route('/profile')
@login_required
def profile():
    from models.models import MealPlan, ExercisePlan
    total_plans = MealPlan.query.filter_by(user_id=current_user.id).count()
    total_logs  = ProgressLog.query.filter_by(user_id=current_user.id).count()
    return render_template('profile.html', total_plans=total_plans, total_logs=total_logs)