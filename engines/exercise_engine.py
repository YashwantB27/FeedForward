import random

def _vid_id(url):
    if 'watch?v=' in url:
        return url.split('watch?v=')[-1]
    if 'youtu.be/' in url:
        return url.split('youtu.be/')[-1]
    return ''

EXERCISES = {
    "lose_weight": {
        "beginner": [
            {"name":"Brisk Walking","sets":1,"reps":"30 mins","cal":150,"muscle":"Full Body","video":"https://youtube.com/watch?v=njeZ29umqVE"},
            {"name":"Jumping Jacks","sets":3,"reps":"20 reps","cal":80,"muscle":"Full Body","video":"https://youtube.com/watch?v=c4DAnQ6DtF8"},
            {"name":"Wall Push-ups","sets":3,"reps":"15 reps","cal":50,"muscle":"Chest","video":"https://youtube.com/watch?v=C5GaGFSRWwA"},
            {"name":"Chair Squats","sets":3,"reps":"15 reps","cal":60,"muscle":"Legs","video":"https://youtube.com/watch?v=N_qYbv7vqms"},
            {"name":"Standing Crunches","sets":3,"reps":"20 reps","cal":40,"muscle":"Core","video":"https://youtube.com/watch?v=9p6zM4GGWSA"},
            {"name":"Step-ups","sets":3,"reps":"15 each leg","cal":70,"muscle":"Legs","video":"https://youtube.com/watch?v=dQqApCGd5Ss"},
            {"name":"Knee Push-ups","sets":3,"reps":"12 reps","cal":45,"muscle":"Chest/Arms","video":"https://youtube.com/watch?v=jWxvty2KROs"},
        ],
        "intermediate": [
            {"name":"Running/Jogging","sets":1,"reps":"30 mins","cal":300,"muscle":"Full Body","video":"https://youtube.com/watch?v=kVnyY17VS9Y"},
            {"name":"Burpees","sets":4,"reps":"15 reps","cal":120,"muscle":"Full Body","video":"https://youtube.com/watch?v=dZgVxmf6jkA"},
            {"name":"Push-ups","sets":4,"reps":"20 reps","cal":80,"muscle":"Chest/Arms","video":"https://youtube.com/watch?v=_l3ySVKYVJ8"},
            {"name":"Squats","sets":4,"reps":"25 reps","cal":100,"muscle":"Legs","video":"https://youtube.com/watch?v=aclHkVaku9U"},
            {"name":"Mountain Climbers","sets":4,"reps":"30 secs","cal":90,"muscle":"Core","video":"https://youtube.com/watch?v=nmwgirgXLYM"},
            {"name":"Plank","sets":3,"reps":"45 secs","cal":50,"muscle":"Core","video":"https://youtube.com/watch?v=ASdvN_XEl_c"},
            {"name":"Lunges","sets":4,"reps":"20 each leg","cal":100,"muscle":"Legs","video":"https://youtube.com/watch?v=QF0BQS2W80k"},
        ],
        "advanced": [
            {"name":"HIIT Sprints","sets":8,"reps":"30s sprint/30s rest","cal":400,"muscle":"Full Body","video":"https://youtube.com/watch?v=ml6cT4AZdqI"},
            {"name":"Box Jumps","sets":5,"reps":"15 reps","cal":150,"muscle":"Legs","video":"https://youtube.com/watch?v=NBY9-kTuHEk"},
            {"name":"Diamond Push-ups","sets":5,"reps":"20 reps","cal":100,"muscle":"Chest/Triceps","video":"https://youtube.com/watch?v=J0DnG1_S92I"},
            {"name":"Jump Squats","sets":5,"reps":"20 reps","cal":140,"muscle":"Legs","video":"https://youtube.com/watch?v=YGGq0AE5Uyc"},
            {"name":"Burpee Pull-ups","sets":4,"reps":"10 reps","cal":130,"muscle":"Full Body","video":"https://youtube.com/watch?v=bCMHHiH2wG4"},
            {"name":"Plank to Push-up","sets":4,"reps":"15 reps","cal":90,"muscle":"Core/Chest","video":"https://youtube.com/watch?v=nMxqKXuAJkQ"},
            {"name":"Speed Skaters","sets":4,"reps":"30 reps","cal":110,"muscle":"Legs/Cardio","video":"https://youtube.com/watch?v=NnFSG5nIEBk"},
        ]
    },
    "gain_muscle": {
        "beginner": [
            {"name":"Push-ups","sets":3,"reps":"10 reps","cal":60,"muscle":"Chest","video":"https://youtube.com/watch?v=_l3ySVKYVJ8"},
            {"name":"Bodyweight Squats","sets":3,"reps":"15 reps","cal":70,"muscle":"Legs","video":"https://youtube.com/watch?v=aclHkVaku9U"},
            {"name":"Dumbbell Bicep Curl","sets":3,"reps":"12 reps","cal":50,"muscle":"Biceps","video":"https://youtube.com/watch?v=ykJmrZ5v0Oo"},
            {"name":"Dumbbell Shoulder Press","sets":3,"reps":"10 reps","cal":60,"muscle":"Shoulders","video":"https://youtube.com/watch?v=qEwKCR5JCog"},
            {"name":"Tricep Dips (Chair)","sets":3,"reps":"12 reps","cal":55,"muscle":"Triceps","video":"https://youtube.com/watch?v=6kALZikXxLc"},
            {"name":"Plank","sets":3,"reps":"30 secs","cal":40,"muscle":"Core","video":"https://youtube.com/watch?v=ASdvN_XEl_c"},
            {"name":"Glute Bridge","sets":3,"reps":"15 reps","cal":55,"muscle":"Glutes","video":"https://youtube.com/watch?v=8bbE64NuDTU"},
        ],
        "intermediate": [
            {"name":"Bench Press (Dumbbell)","sets":4,"reps":"10 reps","cal":90,"muscle":"Chest","video":"https://youtube.com/watch?v=VmB1G1K7v94"},
            {"name":"Pull-ups","sets":4,"reps":"8 reps","cal":100,"muscle":"Back","video":"https://youtube.com/watch?v=eGo4IYlbE5g"},
            {"name":"Barbell Squat","sets":4,"reps":"10 reps","cal":120,"muscle":"Legs","video":"https://youtube.com/watch?v=1oed-UmAxFs"},
            {"name":"Overhead Press","sets":4,"reps":"10 reps","cal":80,"muscle":"Shoulders","video":"https://youtube.com/watch?v=2yjwXTZQDDI"},
            {"name":"Barbell Row","sets":4,"reps":"10 reps","cal":100,"muscle":"Back","video":"https://youtube.com/watch?v=FWJR5Ve8bnQ"},
            {"name":"Romanian Deadlift","sets":4,"reps":"10 reps","cal":110,"muscle":"Hamstrings","video":"https://youtube.com/watch?v=JCXUYuzwNrM"},
            {"name":"Cable Fly","sets":3,"reps":"12 reps","cal":70,"muscle":"Chest","video":"https://youtube.com/watch?v=Iwe6AmxVf7o"},
        ],
        "advanced": [
            {"name":"Deadlift","sets":5,"reps":"5 reps","cal":150,"muscle":"Full Body","video":"https://youtube.com/watch?v=op9kVnSso6Q"},
            {"name":"Barbell Bench Press","sets":5,"reps":"6 reps","cal":120,"muscle":"Chest","video":"https://youtube.com/watch?v=vthMCtgVtFw"},
            {"name":"Weighted Pull-ups","sets":5,"reps":"6 reps","cal":130,"muscle":"Back","video":"https://youtube.com/watch?v=lt2x-E4gJqo"},
            {"name":"Front Squat","sets":5,"reps":"6 reps","cal":140,"muscle":"Legs","video":"https://youtube.com/watch?v=uYumuL_G_V0"},
            {"name":"Arnold Press","sets":4,"reps":"8 reps","cal":100,"muscle":"Shoulders","video":"https://youtube.com/watch?v=6Z15_WdXmVw"},
            {"name":"Weighted Dips","sets":4,"reps":"8 reps","cal":110,"muscle":"Chest/Triceps","video":"https://youtube.com/watch?v=2z8JmcrW-As"},
            {"name":"Barbell Curl","sets":4,"reps":"8 reps","cal":80,"muscle":"Biceps","video":"https://youtube.com/watch?v=kwG2ipFRgfo"},
        ]
    },
    "stay_fit": {
        "beginner": [
            {"name":"20 min Walk","sets":1,"reps":"20 mins","cal":100,"muscle":"Full Body","video":"https://youtube.com/watch?v=njeZ29umqVE"},
            {"name":"Basic Yoga","sets":1,"reps":"20 mins","cal":80,"muscle":"Flexibility","video":"https://youtube.com/watch?v=v7AYKMP6rOE"},
            {"name":"Push-ups","sets":2,"reps":"10 reps","cal":50,"muscle":"Chest","video":"https://youtube.com/watch?v=_l3ySVKYVJ8"},
            {"name":"Squats","sets":2,"reps":"15 reps","cal":60,"muscle":"Legs","video":"https://youtube.com/watch?v=aclHkVaku9U"},
            {"name":"Plank","sets":2,"reps":"30 secs","cal":40,"muscle":"Core","video":"https://youtube.com/watch?v=ASdvN_XEl_c"},
            {"name":"Cycling (light)","sets":1,"reps":"20 mins","cal":120,"muscle":"Cardio","video":"https://youtube.com/watch?v=KNmJGpMKFjw"},
            {"name":"Stretching Routine","sets":1,"reps":"15 mins","cal":50,"muscle":"Flexibility","video":"https://youtube.com/watch?v=L_xrDAtykMI"},
        ],
        "intermediate": [
            {"name":"Jogging","sets":1,"reps":"25 mins","cal":220,"muscle":"Cardio","video":"https://youtube.com/watch?v=kVnyY17VS9Y"},
            {"name":"Push-ups","sets":3,"reps":"15 reps","cal":70,"muscle":"Chest","video":"https://youtube.com/watch?v=_l3ySVKYVJ8"},
            {"name":"Squats","sets":3,"reps":"20 reps","cal":90,"muscle":"Legs","video":"https://youtube.com/watch?v=aclHkVaku9U"},
            {"name":"Plank","sets":3,"reps":"45 secs","cal":50,"muscle":"Core","video":"https://youtube.com/watch?v=ASdvN_XEl_c"},
            {"name":"Lunges","sets":3,"reps":"15 each leg","cal":80,"muscle":"Legs","video":"https://youtube.com/watch?v=QF0BQS2W80k"},
            {"name":"Dumbbell Rows","sets":3,"reps":"12 reps","cal":75,"muscle":"Back","video":"https://youtube.com/watch?v=roCP6wCXPqo"},
            {"name":"Bicycle Crunches","sets":3,"reps":"20 reps","cal":60,"muscle":"Core","video":"https://youtube.com/watch?v=9FGilxCbdz8"},
        ],
        "advanced": [
            {"name":"Running","sets":1,"reps":"30 mins","cal":350,"muscle":"Cardio","video":"https://youtube.com/watch?v=kVnyY17VS9Y"},
            {"name":"Pull-ups","sets":4,"reps":"10 reps","cal":100,"muscle":"Back","video":"https://youtube.com/watch?v=eGo4IYlbE5g"},
            {"name":"Push-ups","sets":4,"reps":"25 reps","cal":90,"muscle":"Chest","video":"https://youtube.com/watch?v=_l3ySVKYVJ8"},
            {"name":"Bulgarian Split Squat","sets":4,"reps":"12 each","cal":120,"muscle":"Legs","video":"https://youtube.com/watch?v=2C-uNgKwPLE"},
            {"name":"Plank Variations","sets":4,"reps":"60 secs","cal":70,"muscle":"Core","video":"https://youtube.com/watch?v=ASdvN_XEl_c"},
            {"name":"Dumbbell Complex","sets":3,"reps":"6 reps each","cal":140,"muscle":"Full Body","video":"https://youtube.com/watch?v=8GHFmFDVWHg"},
            {"name":"Yoga Flow","sets":1,"reps":"20 mins","cal":100,"muscle":"Flexibility","video":"https://youtube.com/watch?v=v7AYKMP6rOE"},
        ]
    }
}

DAY_SPLITS = {
    "gain_muscle": {
        3: ["Chest+Triceps","Back+Biceps","Legs+Shoulders"],
        4: ["Chest+Triceps","Back+Biceps","Legs","Shoulders+Core"],
        5: ["Chest","Back","Legs","Shoulders","Arms+Core"],
        6: ["Chest","Back","Legs","Shoulders","Arms","Full Body"],
    },
    "lose_weight": {
        3: ["Full Body Cardio","Full Body Strength","HIIT Cardio"],
        4: ["Cardio","Full Body","HIIT","Active Recovery"],
        5: ["Cardio","Upper Body","HIIT","Lower Body","Cardio"],
        6: ["HIIT","Upper Body","Cardio","Lower Body","HIIT","Active Recovery"],
    },
    "stay_fit": {
        3: ["Cardio","Full Body","Yoga/Flexibility"],
        4: ["Cardio","Upper Body","Lower Body","Yoga"],
        5: ["Cardio","Upper Body","Cardio","Lower Body","Core+Yoga"],
        6: ["Cardio","Upper Body","Cardio","Lower Body","Full Body","Yoga"],
    }
}

DAYS_OF_WEEK = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']


def generate_exercise_plan(user):
    goal  = user.health_goal   or 'stay_fit'
    level = user.fitness_level or 'beginner'
    days  = user.days_per_week or 4

    if goal  not in EXERCISES:        goal  = 'stay_fit'
    if level not in EXERCISES[goal]:  level = 'beginner'
    if days  not in [3, 4, 5, 6]:     days  = 4

    exercise_pool = EXERCISES[goal][level]
    splits        = DAY_SPLITS.get(goal, DAY_SPLITS['stay_fit']).get(days, DAY_SPLITS['stay_fit'][4])

    # Attach video_id to every exercise, then shuffle
    pool_with_ids = [
        {**ex, 'video_id': _vid_id(ex.get('video', ''))}
        for ex in exercise_pool
    ]
    shuffled_pool   = random.sample(pool_with_ids, len(pool_with_ids))
    shuffled_splits = random.sample(splits, len(splits))

    plan        = []
    split_index = 0

    for day_name in DAYS_OF_WEEK:
        if split_index < len(shuffled_splits):
            focus = shuffled_splits[split_index]
            start = (split_index * 3) % len(shuffled_pool)
            exs   = [shuffled_pool[(start + j) % len(shuffled_pool)] for j in range(3)]
            total_cal = sum(e['cal'] for e in exs)
            plan.append({
                'day':            day_name,
                'type':           'workout',
                'focus':          focus,
                'exercises':      exs,
                'total_calories': total_cal,
                'duration':       f"{len(exs) * 12}-{len(exs) * 18} mins",
            })
            split_index += 1
        else:
            plan.append({
                'day':            day_name,
                'type':           'rest',
                'focus':          'Rest & Recovery',
                'exercises':      [],
                'total_calories': 0,
                'duration':       'Rest',
            })

    return {
        'plan':          plan,
        'goal':          goal,
        'level':         level,
        'days_per_week': days,
    }


def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    if   bmi < 18.5: cat = ('Underweight',  'info',    'Increase calorie intake with nutritious foods')
    elif bmi < 25:   cat = ('Normal Weight', 'success', 'Maintain your current healthy lifestyle')
    elif bmi < 30:   cat = ('Overweight',    'warning', 'Consider the Lose Weight plan')
    else:            cat = ('Obese',         'danger',  'Start with beginner cardio and consult a doctor')
    healthy_min = round(18.5 * (height_m ** 2), 1)
    healthy_max = round(24.9 * (height_m ** 2), 1)
    return {
        'bmi':         round(bmi, 1),
        'category':    cat[0],
        'class':       cat[1],
        'advice':      cat[2],
        'healthy_min': healthy_min,
        'healthy_max': healthy_max,
    }


def calculate_water_intake(weight, workout_done=False):
    base = weight * 0.033
    if workout_done:
        base += 0.5
    return round(base, 1)