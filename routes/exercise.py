from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from extensions import db
from models.models import ExercisePlan, CustomWorkout
from engines.exercise_engine import generate_exercise_plan, calculate_bmi, calculate_water_intake
import json

exercise = Blueprint('exercise', __name__, url_prefix='/exercise')

EXERCISE_LIBRARY = [
    {'name':'Brisk Walking',       'category':'Cardio',     'cal':150,'sets':1,'reps':'30 min', 'muscle':'Full Body'},
    {'name':'Jogging',             'category':'Cardio',     'cal':220,'sets':1,'reps':'25 min', 'muscle':'Full Body'},
    {'name':'Jump Rope',           'category':'Cardio',     'cal':300,'sets':3,'reps':'3 min',  'muscle':'Full Body'},
    {'name':'Cycling',             'category':'Cardio',     'cal':250,'sets':1,'reps':'30 min', 'muscle':'Legs'},
    {'name':'HIIT Sprints',        'category':'Cardio',     'cal':400,'sets':6,'reps':'30 sec', 'muscle':'Full Body'},
    {'name':'Burpees',             'category':'Cardio',     'cal':120,'sets':4,'reps':'15',     'muscle':'Full Body'},
    {'name':'Push-Ups',            'category':'Strength',   'cal':50, 'sets':3,'reps':'15',     'muscle':'Chest'},
    {'name':'Pull-Ups',            'category':'Strength',   'cal':60, 'sets':3,'reps':'10',     'muscle':'Back'},
    {'name':'Squats',              'category':'Strength',   'cal':70, 'sets':4,'reps':'15',     'muscle':'Legs'},
    {'name':'Lunges',              'category':'Strength',   'cal':60, 'sets':3,'reps':'12',     'muscle':'Legs'},
    {'name':'Deadlift',            'category':'Strength',   'cal':150,'sets':5,'reps':'5',      'muscle':'Full Body'},
    {'name':'Bench Press',         'category':'Strength',   'cal':120,'sets':4,'reps':'10',     'muscle':'Chest'},
    {'name':'Shoulder Press',      'category':'Strength',   'cal':100,'sets':3,'reps':'12',     'muscle':'Shoulders'},
    {'name':'Bicep Curl',          'category':'Strength',   'cal':80, 'sets':3,'reps':'12',     'muscle':'Biceps'},
    {'name':'Tricep Dips',         'category':'Strength',   'cal':70, 'sets':3,'reps':'15',     'muscle':'Triceps'},
    {'name':'Glute Bridge',        'category':'Strength',   'cal':55, 'sets':3,'reps':'15',     'muscle':'Glutes'},
    {'name':'Dumbbell Rows',       'category':'Strength',   'cal':75, 'sets':3,'reps':'12',     'muscle':'Back'},
    {'name':'Plank',               'category':'Core',       'cal':40, 'sets':3,'reps':'60 sec', 'muscle':'Core'},
    {'name':'Crunches',            'category':'Core',       'cal':35, 'sets':3,'reps':'20',     'muscle':'Core'},
    {'name':'Mountain Climbers',   'category':'Core',       'cal':90, 'sets':3,'reps':'30 sec', 'muscle':'Core'},
    {'name':'Leg Raises',          'category':'Core',       'cal':45, 'sets':3,'reps':'15',     'muscle':'Core'},
    {'name':'Bicycle Crunches',    'category':'Core',       'cal':55, 'sets':3,'reps':'20',     'muscle':'Core'},
    {'name':'Yoga Sun Salutation', 'category':'Flexibility','cal':80, 'sets':5,'reps':'rounds', 'muscle':'Full Body'},
    {'name':'Hamstring Stretch',   'category':'Flexibility','cal':20, 'sets':2,'reps':'60 sec', 'muscle':'Legs'},
    {'name':'Hip Flexor Stretch',  'category':'Flexibility','cal':20, 'sets':2,'reps':'60 sec', 'muscle':'Hips'},
    {'name':'Child\'s Pose',       'category':'Flexibility','cal':15, 'sets':1,'reps':'5 min',  'muscle':'Back'},
    {'name':'Foam Rolling',        'category':'Flexibility','cal':30, 'sets':1,'reps':'10 min', 'muscle':'Full Body'},
]

# YouTube video IDs for exercises (popup player)
YOUTUBE_MAP = {
    'Brisk Walking':       'njeZ29umqVE',
    'Jogging':             'kVnyY17VS9Y',
    'Running/Jogging':     'kVnyY17VS9Y',
    'Jump Rope':           'FJmRQ5iTXKE',
    'Push-Ups':            '_l3ySVKYVJ8',
    'Pull-Ups':            'eGo4IYlbE5g',
    'Squats':              'aclHkVaku9U',
    'Bodyweight Squats':   'aclHkVaku9U',
    'Deadlift':            'op9kVnSso6Q',
    'Bench Press':         'rT7DgCr-3pg',
    'Plank':               'ASdvN_XEl_c',
    'Yoga Sun Salutation': '73sjOu0g58M',
    'Lunges':              'QF0BQS2W80k',
    'Crunches':            'Xyd_fa5zoEU',
    'Burpees':             'dZgVxmf6jkA',
    'Mountain Climbers':   'nmwgirgXLYM',
    'Bicycle Crunches':    '9FGilxCbdz8',
    'Shoulder Press':      '2yjwXTZQDDI',
    'Dumbbell Shoulder Press': 'qEwKCR5JCog',
    'Bicep Curl':          'ykJmrZ5v0Oo',
    'Dumbbell Bicep Curl': 'ykJmrZ5v0Oo',
    'Glute Bridge':        '8bbE64NuDTU',
    'Dumbbell Rows':       'roCP6wCXPqo',
    'HIIT Sprints':        'ml6cT4AZdqI',
    'HIIT Sprint Intervals':'ml6cT4AZdqI',
    'Jumping Jacks':       'c4DAnQ6DtF8',
    'Box Jumps':           'NBY9-kTuHEk',
    'Tricep Dips (Chair)': '6kALZikXxLc',
    'Leg Raises':          'JB2oyawG9KQ',
    'Basic Yoga':          'v7AYKMP6rOE',
}

def enrich_plan(plan_data):
    """Attach YouTube video IDs to every exercise. Engine uses 'plan' key."""
    if not plan_data:
        return plan_data
    for day in plan_data.get('plan', []):
        for ex in day.get('exercises', []):
            ex['video_id'] = YOUTUBE_MAP.get(ex.get('name', ''))
    return plan_data

@exercise.route('/')
@login_required
def index():
    plan       = ExercisePlan.query.filter_by(user_id=current_user.id)\
                                   .order_by(ExercisePlan.created_at.desc()).first()
    plan_data  = enrich_plan(json.loads(plan.plan_json)) if plan and plan.plan_json else None
    bmi_data   = calculate_bmi(current_user.weight or 70, current_user.height or 170) \
                 if current_user.weight and current_user.height else None
    water      = calculate_water_intake(current_user.weight or 70, False)
    custom_wos = CustomWorkout.query.filter_by(user_id=current_user.id)\
                                    .order_by(CustomWorkout.created_at.desc()).all()
    return render_template('exercise/index.html',
                           plan=plan, plan_data=plan_data,
                           bmi_data=bmi_data, water=water,
                           custom_workouts=custom_wos,
                           exercise_library=EXERCISE_LIBRARY)

@exercise.route('/regenerate')
@login_required
def regenerate():
    plan_data = generate_exercise_plan(current_user)
    existing  = ExercisePlan.query.filter_by(user_id=current_user.id).first()
    if existing:
        existing.plan_json = json.dumps(plan_data)
    else:
        db.session.add(ExercisePlan(
            user_id       = current_user.id,
            plan_json     = json.dumps(plan_data),
            fitness_goal  = current_user.health_goal,
            fitness_level = current_user.fitness_level,
            days_per_week = current_user.days_per_week,
        ))
    db.session.commit()
    flash('New exercise plan generated! 💪', 'success')
    return redirect(url_for('exercise.index'))

@exercise.route('/edit-exercise', methods=['POST'])
@login_required
def edit_exercise():
    """AJAX: edit a single exercise inside the AI plan."""
    data       = request.get_json()
    day_idx    = int(data.get('day', 0))
    ex_idx     = int(data.get('ex', 0))
    new_name   = data.get('name', '').strip()
    new_sets   = data.get('sets', 3)
    new_reps   = data.get('reps', '').strip()
    new_cal    = int(data.get('cal', 0))
    new_muscle = data.get('muscle', '').strip()

    plan = ExercisePlan.query.filter_by(user_id=current_user.id)\
                             .order_by(ExercisePlan.created_at.desc()).first()
    if not plan:
        return jsonify({'ok': False, 'msg': 'No plan found'})

    plan_data = json.loads(plan.plan_json)
    days = plan_data.get('plan', [])          # engine stores under 'plan' key
    if 0 <= day_idx < len(days):
        exs = days[day_idx].get('exercises', [])
        if 0 <= ex_idx < len(exs):
            exs[ex_idx].update({
                'name': new_name, 'sets': new_sets,
                'reps': new_reps, 'cal':  new_cal,
                'muscle': new_muscle,
            })
            plan.plan_json = json.dumps(plan_data)
            db.session.commit()
            return jsonify({'ok': True})
    return jsonify({'ok': False, 'msg': 'Invalid index'})

@exercise.route('/save-custom', methods=['POST'])
@login_required
def save_custom():
    data = request.get_json()
    name = data.get('name', '').strip()
    exs  = data.get('exercises', [])
    if not name or not exs:
        return jsonify({'ok': False, 'msg': 'Name and at least one exercise required'})
    wo = CustomWorkout(user_id=current_user.id, name=name, exercises=json.dumps(exs))
    db.session.add(wo)
    db.session.commit()
    return jsonify({'ok': True, 'id': wo.id, 'name': wo.name})

@exercise.route('/delete-custom/<int:wo_id>', methods=['POST'])
@login_required
def delete_custom(wo_id):
    wo = CustomWorkout.query.filter_by(id=wo_id, user_id=current_user.id).first_or_404()
    db.session.delete(wo)
    db.session.commit()
    return jsonify({'ok': True})
