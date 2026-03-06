import random
import json

# ── Complete Meal Database ────────────────────────────────────────────────────
MEALS = {
    "veg": {
        "lose_weight": {
            "breakfast": [
                {"name":"Oats with Berries","cal":280,"protein":10,"carbs":45,"fat":6,"carbon":0.3},
                {"name":"Moong Dal Chilla","cal":200,"protein":12,"carbs":30,"fat":4,"carbon":0.2},
                {"name":"Vegetable Poha","cal":220,"protein":6,"carbs":40,"fat":5,"carbon":0.2},
                {"name":"Sprouts Salad Bowl","cal":180,"protein":10,"carbs":28,"fat":3,"carbon":0.1},
                {"name":"Idli with Sambar","cal":260,"protein":9,"carbs":48,"fat":3,"carbon":0.2},
                {"name":"Greek Yogurt Parfait","cal":250,"protein":15,"carbs":35,"fat":4,"carbon":0.4},
                {"name":"Upma with Vegetables","cal":240,"protein":8,"carbs":38,"fat":6,"carbon":0.3},
            ],
            "lunch": [
                {"name":"Dal + Brown Rice + Salad","cal":420,"protein":18,"carbs":65,"fat":8,"carbon":0.5},
                {"name":"Palak Paneer + Roti","cal":480,"protein":22,"carbs":55,"fat":14,"carbon":0.8},
                {"name":"Rajma Chawal","cal":450,"protein":20,"carbs":70,"fat":9,"carbon":0.6},
                {"name":"Vegetable Khichdi","cal":380,"protein":14,"carbs":62,"fat":7,"carbon":0.4},
                {"name":"Chole + 2 Chapati","cal":460,"protein":19,"carbs":68,"fat":10,"carbon":0.5},
                {"name":"Sambar Rice","cal":390,"protein":13,"carbs":70,"fat":6,"carbon":0.3},
                {"name":"Mixed Veg Curry + Rice","cal":400,"protein":12,"carbs":65,"fat":8,"carbon":0.4},
            ],
            "dinner": [
                {"name":"Vegetable Soup + 2 Rotis","cal":320,"protein":10,"carbs":52,"fat":6,"carbon":0.3},
                {"name":"Tofu Stir Fry + Quinoa","cal":380,"protein":22,"carbs":45,"fat":12,"carbon":0.5},
                {"name":"Lentil Soup + Bread","cal":340,"protein":18,"carbs":50,"fat":5,"carbon":0.3},
                {"name":"Mixed Dal + 2 Rotis","cal":360,"protein":16,"carbs":55,"fat":7,"carbon":0.4},
                {"name":"Vegetable Daliya","cal":300,"protein":10,"carbs":50,"fat":5,"carbon":0.2},
                {"name":"Mushroom Curry + Rice","cal":350,"protein":14,"carbs":55,"fat":8,"carbon":0.4},
                {"name":"Paneer Bhurji + 2 Rotis","cal":400,"protein":24,"carbs":38,"fat":16,"carbon":0.7},
            ],
            "snack": [
                {"name":"Apple + Almonds","cal":180,"carbon":0.2},
                {"name":"Roasted Chana","cal":150,"carbon":0.1},
                {"name":"Cucumber + Hummus","cal":130,"carbon":0.2},
                {"name":"Banana + Peanut Butter","cal":200,"carbon":0.3},
                {"name":"Mixed Nuts","cal":170,"carbon":0.2},
                {"name":"Coconut Water","cal":90,"carbon":0.1},
                {"name":"Fruit Chaat","cal":140,"carbon":0.1},
            ]
        },
        "gain_muscle": {
            "breakfast": [
                {"name":"Paneer Scramble + Toast","cal":420,"protein":28,"carbs":35,"fat":18,"carbon":0.8},
                {"name":"Protein Smoothie + Oats","cal":480,"protein":32,"carbs":55,"fat":10,"carbon":0.5},
                {"name":"Tofu Scramble + Brown Bread","cal":400,"protein":26,"carbs":38,"fat":14,"carbon":0.6},
                {"name":"Soya Chunk Upma","cal":380,"protein":25,"carbs":45,"fat":8,"carbon":0.3},
                {"name":"Peanut Butter Banana Shake","cal":450,"protein":20,"carbs":60,"fat":16,"carbon":0.4},
                {"name":"Rajgira Chilla + Curd","cal":340,"protein":18,"carbs":40,"fat":10,"carbon":0.3},
                {"name":"Greek Yogurt + Nuts + Fruits","cal":360,"protein":22,"carbs":48,"fat":8,"carbon":0.5},
            ],
            "lunch": [
                {"name":"Soya Curry + Rice + Dal","cal":620,"protein":35,"carbs":80,"fat":12,"carbon":0.6},
                {"name":"Paneer Tikka + Roti + Curd","cal":680,"protein":40,"carbs":60,"fat":22,"carbon":1.0},
                {"name":"Rajma + Rice + Raita","cal":640,"protein":32,"carbs":85,"fat":10,"carbon":0.7},
                {"name":"Tofu Biryani + Raita","cal":580,"protein":30,"carbs":78,"fat":14,"carbon":0.6},
                {"name":"Mixed Dal + Rice + Sabzi","cal":600,"protein":26,"carbs":82,"fat":11,"carbon":0.5},
                {"name":"Palak Paneer + 3 Rotis","cal":650,"protein":34,"carbs":65,"fat":20,"carbon":0.9},
                {"name":"Chhole + Bhature","cal":720,"protein":28,"carbs":95,"fat":18,"carbon":0.8},
            ],
            "dinner": [
                {"name":"Paneer Curry + Quinoa","cal":560,"protein":38,"carbs":55,"fat":18,"carbon":0.8},
                {"name":"Dal Makhani + 3 Rotis","cal":580,"protein":28,"carbs":72,"fat":16,"carbon":0.7},
                {"name":"Soya Keema + Roti","cal":520,"protein":35,"carbs":50,"fat":15,"carbon":0.5},
                {"name":"Tofu Stir Fry + Brown Rice","cal":500,"protein":32,"carbs":60,"fat":14,"carbon":0.6},
                {"name":"Chana Masala + Rice","cal":540,"protein":26,"carbs":75,"fat":10,"carbon":0.6},
                {"name":"Paneer Bhurji + 3 Rotis","cal":600,"protein":36,"carbs":58,"fat":22,"carbon":0.9},
                {"name":"Mushroom Palak + Rice","cal":480,"protein":22,"carbs":65,"fat":12,"carbon":0.4},
            ],
            "snack": [
                {"name":"Protein Shake + Banana","cal":280,"carbon":0.4},
                {"name":"Peanut Butter on Toast","cal":260,"carbon":0.3},
                {"name":"Mixed Nuts + Milk","cal":300,"carbon":0.5},
                {"name":"Curd + Fruits","cal":220,"carbon":0.3},
                {"name":"Roasted Chickpeas","cal":200,"carbon":0.2},
                {"name":"Cheese Sandwich","cal":280,"carbon":0.5},
                {"name":"Soya Milk Smoothie","cal":250,"carbon":0.3},
            ]
        },
        "stay_fit": {
            "breakfast": [
                {"name":"Idli + Sambar + Chutney","cal":300,"protein":10,"carbs":55,"fat":5,"carbon":0.3},
                {"name":"Vegetable Paratha + Curd","cal":350,"protein":10,"carbs":52,"fat":10,"carbon":0.4},
                {"name":"Dosa + Sambar","cal":280,"protein":8,"carbs":50,"fat":6,"carbon":0.3},
                {"name":"Poha + Chai","cal":260,"protein":6,"carbs":48,"fat":6,"carbon":0.2},
                {"name":"Masala Oats","cal":300,"protein":9,"carbs":50,"fat":7,"carbon":0.3},
                {"name":"Banana Smoothie","cal":280,"protein":8,"carbs":52,"fat":5,"carbon":0.2},
                {"name":"Rava Upma + Chutney","cal":310,"protein":7,"carbs":54,"fat":7,"carbon":0.3},
            ],
            "lunch": [
                {"name":"Dal + Rice + Salad","cal":480,"protein":16,"carbs":75,"fat":8,"carbon":0.5},
                {"name":"Vegetable Biryani + Raita","cal":520,"protein":14,"carbs":82,"fat":12,"carbon":0.5},
                {"name":"Dal-Sabzi-Roti Thali","cal":550,"protein":18,"carbs":80,"fat":12,"carbon":0.6},
                {"name":"Curd Rice + Pickle","cal":420,"protein":12,"carbs":72,"fat":8,"carbon":0.4},
                {"name":"Sambar + Rice + Papad","cal":460,"protein":14,"carbs":78,"fat":7,"carbon":0.4},
                {"name":"Aloo Matar + Roti","cal":500,"protein":13,"carbs":75,"fat":12,"carbon":0.5},
                {"name":"Pulao + Raita","cal":480,"protein":12,"carbs":78,"fat":10,"carbon":0.4},
            ],
            "dinner": [
                {"name":"Khichdi + Pickle","cal":380,"protein":14,"carbs":65,"fat":7,"carbon":0.3},
                {"name":"Roti + Sabzi + Dal","cal":420,"protein":16,"carbs":62,"fat":9,"carbon":0.4},
                {"name":"Vegetable Soup + Roti","cal":340,"protein":10,"carbs":54,"fat":6,"carbon":0.3},
                {"name":"Dal + 2 Rotis","cal":360,"protein":16,"carbs":55,"fat":6,"carbon":0.3},
                {"name":"Mixed Veg + Rice","cal":380,"protein":11,"carbs":65,"fat":7,"carbon":0.3},
                {"name":"Rajma + Roti","cal":420,"protein":18,"carbs":60,"fat":8,"carbon":0.5},
                {"name":"Paneer Roti Roll","cal":400,"protein":20,"carbs":48,"fat":14,"carbon":0.6},
            ],
            "snack": [
                {"name":"Chai + 2 Biscuits","cal":160,"carbon":0.2},
                {"name":"Seasonal Fruits","cal":120,"carbon":0.1},
                {"name":"Roasted Makhana","cal":130,"carbon":0.1},
                {"name":"Buttermilk","cal":80,"carbon":0.1},
                {"name":"Fruit Chaat","cal":140,"carbon":0.1},
                {"name":"Coconut Water","cal":90,"carbon":0.1},
                {"name":"Popcorn","cal":100,"carbon":0.1},
            ]
        }
    },
    "non_veg": {
        "lose_weight": {
            "breakfast": [
                {"name":"Egg White Omelette + Toast","cal":280,"protein":22,"carbs":28,"fat":8,"carbon":0.6},
                {"name":"Boiled Eggs + Oats","cal":300,"protein":20,"carbs":40,"fat":10,"carbon":0.7},
                {"name":"Egg Bhurji + Roti","cal":310,"protein":18,"carbs":32,"fat":12,"carbon":0.8},
                {"name":"Tuna Salad Bowl","cal":260,"protein":30,"carbs":10,"fat":10,"carbon":0.9},
                {"name":"Poached Eggs + Vegetables","cal":240,"protein":16,"carbs":18,"fat":10,"carbon":0.6},
                {"name":"Grilled Chicken Sandwich","cal":320,"protein":28,"carbs":30,"fat":8,"carbon":1.2},
                {"name":"Chicken Upma","cal":340,"protein":24,"carbs":38,"fat":10,"carbon":1.1},
            ],
            "lunch": [
                {"name":"Grilled Chicken + Salad + Rice","cal":480,"protein":40,"carbs":50,"fat":10,"carbon":2.0},
                {"name":"Fish Curry + Brown Rice","cal":460,"protein":38,"carbs":52,"fat":12,"carbon":1.5},
                {"name":"Egg Curry + Rice","cal":460,"protein":24,"carbs":58,"fat":14,"carbon":1.0},
                {"name":"Chicken Soup + Bread","cal":380,"protein":32,"carbs":35,"fat":8,"carbon":1.5},
                {"name":"Prawn Stir Fry + Rice","cal":440,"protein":35,"carbs":52,"fat":10,"carbon":1.3},
                {"name":"Fish + Dal + Rice","cal":500,"protein":36,"carbs":55,"fat":12,"carbon":1.8},
                {"name":"Chicken Biryani (light)","cal":520,"protein":38,"carbs":62,"fat":12,"carbon":2.2},
            ],
            "dinner": [
                {"name":"Baked Fish + Vegetables","cal":380,"protein":40,"carbs":20,"fat":12,"carbon":1.4},
                {"name":"Chicken Tikka + Salad","cal":360,"protein":42,"carbs":15,"fat":12,"carbon":1.8},
                {"name":"Grilled Fish + Roti","cal":380,"protein":38,"carbs":30,"fat":10,"carbon":1.4},
                {"name":"Egg Fried Rice (light)","cal":400,"protein":18,"carbs":55,"fat":12,"carbon":0.9},
                {"name":"Prawn Curry + Rice","cal":440,"protein":30,"carbs":55,"fat":12,"carbon":1.3},
                {"name":"Chicken Soup + 2 Rotis","cal":420,"protein":34,"carbs":45,"fat":10,"carbon":1.6},
                {"name":"Grilled Chicken + Quinoa","cal":460,"protein":44,"carbs":42,"fat":10,"carbon":2.0},
            ],
            "snack": [
                {"name":"Boiled Eggs x2","cal":140,"carbon":0.6},
                {"name":"Tuna on Crackers","cal":180,"carbon":0.8},
                {"name":"Greek Yogurt","cal":130,"carbon":0.5},
                {"name":"Chicken Strips","cal":170,"carbon":1.1},
                {"name":"Fish Cutlet","cal":150,"carbon":0.7},
                {"name":"Egg Whites","cal":100,"carbon":0.4},
                {"name":"Chicken Jerky","cal":160,"carbon":1.0},
            ]
        },
        "gain_muscle": {
            "breakfast": [
                {"name":"4 Eggs + Oats + Milk","cal":520,"protein":40,"carbs":55,"fat":16,"carbon":1.4},
                {"name":"Chicken Omelette + Toast","cal":480,"protein":42,"carbs":32,"fat":18,"carbon":1.8},
                {"name":"Scrambled Eggs + Paneer","cal":500,"protein":38,"carbs":18,"fat":24,"carbon":1.5},
                {"name":"Protein Shake + Boiled Eggs + Banana","cal":560,"protein":50,"carbs":52,"fat":14,"carbon":1.2},
                {"name":"Chicken Paratha + Curd","cal":580,"protein":36,"carbs":60,"fat":18,"carbon":2.0},
                {"name":"Egg Bhurji + 3 Rotis","cal":500,"protein":28,"carbs":55,"fat":18,"carbon":1.0},
                {"name":"Tuna Sandwich + Milk","cal":520,"protein":44,"carbs":48,"fat":14,"carbon":1.6},
            ],
            "lunch": [
                {"name":"Chicken Breast + Rice + Dal","cal":720,"protein":55,"carbs":80,"fat":14,"carbon":2.5},
                {"name":"Fish + Rice + Vegetables","cal":660,"protein":50,"carbs":75,"fat":14,"carbon":1.8},
                {"name":"Chicken Biryani + Raita","cal":750,"protein":52,"carbs":80,"fat":20,"carbon":2.8},
                {"name":"Egg Biryani + Raita","cal":680,"protein":36,"carbs":82,"fat":18,"carbon":1.4},
                {"name":"Mutton Curry + Rice","cal":780,"protein":48,"carbs":75,"fat":22,"carbon":3.5},
                {"name":"Prawn Biryani","cal":700,"protein":48,"carbs":78,"fat":16,"carbon":2.0},
                {"name":"Chicken Thali","cal":760,"protein":50,"carbs":82,"fat":18,"carbon":2.6},
            ],
            "dinner": [
                {"name":"Grilled Chicken + Sweet Potato","cal":620,"protein":55,"carbs":55,"fat":12,"carbon":2.2},
                {"name":"Fish Curry + 3 Rotis","cal":600,"protein":48,"carbs":60,"fat":16,"carbon":1.8},
                {"name":"Chicken Stew + Rice","cal":640,"protein":52,"carbs":65,"fat":14,"carbon":2.3},
                {"name":"Prawn Masala + Rice","cal":580,"protein":44,"carbs":62,"fat":14,"carbon":1.8},
                {"name":"Chicken Palak + Quinoa","cal":600,"protein":54,"carbs":52,"fat":16,"carbon":2.4},
                {"name":"Egg Curry + 3 Rotis","cal":560,"protein":32,"carbs":62,"fat":18,"carbon":1.2},
                {"name":"Mutton Keema + Roti","cal":680,"protein":46,"carbs":50,"fat":24,"carbon":3.2},
            ],
            "snack": [
                {"name":"Protein Shake + Banana","cal":300,"carbon":0.8},
                {"name":"Boiled Eggs x3","cal":210,"carbon":0.9},
                {"name":"Chicken Strips","cal":250,"carbon":1.4},
                {"name":"Tuna + Rice Cakes","cal":240,"carbon":0.9},
                {"name":"Milk + Nuts","cal":280,"carbon":0.7},
                {"name":"Greek Yogurt + Berries","cal":220,"carbon":0.5},
                {"name":"Egg Sandwich","cal":260,"carbon":0.8},
            ]
        },
        "stay_fit": {
            "breakfast": [
                {"name":"2 Eggs + Toast","cal":340,"protein":16,"carbs":40,"fat":12,"carbon":0.8},
                {"name":"Omelette + Poha","cal":360,"protein":18,"carbs":50,"fat":12,"carbon":0.7},
                {"name":"Boiled Eggs + Banana","cal":280,"protein":14,"carbs":38,"fat":8,"carbon":0.6},
                {"name":"Chicken Sandwich","cal":380,"protein":28,"carbs":38,"fat":12,"carbon":1.4},
                {"name":"Egg Dosa","cal":320,"protein":14,"carbs":48,"fat":10,"carbon":0.6},
                {"name":"Fish Poha","cal":350,"protein":22,"carbs":46,"fat":10,"carbon":1.0},
                {"name":"Egg Paratha + Curd","cal":380,"protein":16,"carbs":50,"fat":14,"carbon":0.8},
            ],
            "lunch": [
                {"name":"Dal + Rice + Chicken Curry","cal":580,"protein":38,"carbs":72,"fat":14,"carbon":2.0},
                {"name":"Fish + Rice + Salad","cal":540,"protein":40,"carbs":65,"fat":12,"carbon":1.6},
                {"name":"Egg Curry + Rice","cal":520,"protein":24,"carbs":68,"fat":15,"carbon":1.0},
                {"name":"Chicken Roti Roll","cal":560,"protein":36,"carbs":58,"fat":15,"carbon":1.8},
                {"name":"Prawn + Rice + Sabzi","cal":520,"protein":34,"carbs":65,"fat":12,"carbon":1.4},
                {"name":"Fish Biryani","cal":580,"protein":40,"carbs":68,"fat":14,"carbon":1.8},
                {"name":"Mixed Chicken Thali","cal":600,"protein":38,"carbs":72,"fat":16,"carbon":2.0},
            ],
            "dinner": [
                {"name":"Grilled Fish + Vegetables","cal":420,"protein":38,"carbs":25,"fat":14,"carbon":1.4},
                {"name":"Chicken Soup + Bread","cal":400,"protein":32,"carbs":40,"fat":10,"carbon":1.5},
                {"name":"Egg Fried Rice","cal":460,"protein":18,"carbs":62,"fat":14,"carbon":0.9},
                {"name":"Fish Masala + 2 Rotis","cal":440,"protein":35,"carbs":42,"fat":12,"carbon":1.4},
                {"name":"Prawn Stir Fry + Rice","cal":460,"protein":32,"carbs":55,"fat":12,"carbon":1.3},
                {"name":"Chicken Palak + Roti","cal":480,"protein":40,"carbs":38,"fat":16,"carbon":2.0},
                {"name":"Chicken Roti + Salad","cal":480,"protein":36,"carbs":45,"fat":14,"carbon":1.8},
            ],
            "snack": [
                {"name":"Boiled Egg + Fruit","cal":180,"carbon":0.5},
                {"name":"Chicken Salad","cal":200,"carbon":1.2},
                {"name":"Tuna Crackers","cal":160,"carbon":0.7},
                {"name":"Greek Yogurt","cal":130,"carbon":0.5},
                {"name":"Fish Fingers x2","cal":180,"carbon":0.8},
                {"name":"Milk + Banana","cal":200,"carbon":0.5},
                {"name":"Egg Whites + Nuts","cal":190,"carbon":0.5},
            ]
        }
    }
}

# ── Allergen keyword map ──────────────────────────────────────────────────────
ALLERGEN_MAP = {
    'gluten':  ['wheat', 'bread', 'pasta', 'roti', 'oats', 'semolina', 'maida',
                'toast', 'paratha', 'upma', 'rava', 'daliya', 'biscuit', 'sandwich',
                'bhature', 'dosa', 'idli', 'poha', 'chapati'],
    'dairy':   ['milk', 'paneer', 'curd', 'cheese', 'butter', 'ghee', 'yogurt',
                'cream', 'raita', 'lassi', 'buttermilk', 'makhani', 'greek yogurt'],
    'nuts':    ['almond', 'peanut', 'cashew', 'walnut', 'pistachio', 'nut',
                'peanut butter'],
    'egg':     ['egg'],
    'soy':     ['tofu', 'soya', 'soy'],
    'seafood': ['fish', 'prawn', 'shrimp', 'tuna', 'salmon'],
}

def meal_has_allergen(meal_name: str, user_allergies: list) -> bool:
    """Return True if the meal name contains any ingredient the user is allergic to."""
    if not user_allergies:
        return False
    name_lower = meal_name.lower()
    for allergen in user_allergies:
        keywords = ALLERGEN_MAP.get(allergen, [])
        if any(kw in name_lower for kw in keywords):
            return True
    return False

def filter_meals(meal_list: list, user_allergies: list) -> list:
    """
    Remove meals that contain the user's allergens.
    Falls back to the full list if filtering removes everything
    (so the plan never crashes).
    """
    if not user_allergies:
        return meal_list
    safe = [m for m in meal_list if not meal_has_allergen(m['name'], user_allergies)]
    return safe if safe else meal_list  # graceful fallback

def tag_allergens(meal_name: str) -> list:
    """Return list of allergen keys present in a meal name (for display)."""
    name_lower = meal_name.lower()
    return [a for a, kws in ALLERGEN_MAP.items() if any(k in name_lower for k in kws)]

# ── Harris-Benedict BMR ───────────────────────────────────────────────────────
def calculate_bmr(age, weight, height, gender='male'):
    if gender == 'female':
        return 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)
    return 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)

def calculate_daily_calories(bmr, goal):
    tdee = bmr * 1.375
    return {'lose_weight': tdee - 500, 'gain_muscle': tdee + 300, 'stay_fit': tdee}.get(goal, tdee)

def get_carbon_label(score):
    if score < 0.5:  return ('🟢 Low',    'success')
    if score < 1.5:  return ('🟡 Medium', 'warning')
    return                  ('🔴 High',   'danger')

# ── Main plan generator ───────────────────────────────────────────────────────
def generate_meal_plan(user):
    pref   = getattr(user, 'dietary_pref', None) or 'veg'
    goal   = getattr(user, 'health_goal',  None) or 'stay_fit'
    age    = getattr(user, 'age',          None) or 25
    wt     = getattr(user, 'weight',       None) or 70
    ht     = getattr(user, 'height',       None) or 170
    gender = getattr(user, 'gender',       None) or 'male'

    # ── Read user allergies from profile ─────────────────────────────────────
    raw_allergies = getattr(user, 'allergies', '') or ''
    user_allergies = [a.strip().lower() for a in raw_allergies.split(',') if a.strip()]

    meal_key   = 'non_veg' if pref == 'non_veg' else 'veg'
    bmr        = calculate_bmr(age, wt, ht, gender)
    target_cal = calculate_daily_calories(bmr, goal)
    meals_pool = MEALS.get(meal_key, MEALS['veg']).get(goal, MEALS['veg']['stay_fit'])

    # ── Filter each slot to remove allergen-containing meals ─────────────────
    safe_pool = {
        slot: filter_meals(meals_pool[slot], user_allergies)
        for slot in ['breakfast', 'lunch', 'dinner', 'snack']
    }

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    plan = []

    # Shuffle safe pool so every regenerate gives a fresh plan
    shuffled = {
        slot: random.sample(safe_pool[slot], len(safe_pool[slot]))
        for slot in ['breakfast', 'lunch', 'dinner', 'snack']
    }

    for i, day in enumerate(days):
        breakfast = shuffled['breakfast'][i % len(shuffled['breakfast'])]
        lunch     = shuffled['lunch'][i % len(shuffled['lunch'])]
        dinner    = shuffled['dinner'][i % len(shuffled['dinner'])]
        snack     = shuffled['snack'][i % len(shuffled['snack'])]

        day_carbon  = breakfast['carbon'] + lunch['carbon'] + dinner['carbon'] + snack['carbon']
        day_cal     = breakfast['cal']    + lunch['cal']    + dinner['cal']    + snack['cal']
        day_protein = (breakfast.get('protein', 0) + lunch.get('protein', 0)
                       + dinner.get('protein', 0))

        plan.append({
            'day':            day,
            'breakfast':      {**breakfast, 'allergens': tag_allergens(breakfast['name'])},
            'lunch':          {**lunch,     'allergens': tag_allergens(lunch['name'])},
            'dinner':         {**dinner,    'allergens': tag_allergens(dinner['name'])},
            'snack':          {**snack,     'allergens': tag_allergens(snack['name'])},
            'total_calories': day_cal,
            'total_protein':  day_protein,
            'total_carbon':   round(day_carbon, 2),
            'carbon_label':   get_carbon_label(day_carbon)[0],
            'carbon_class':   get_carbon_label(day_carbon)[1],
        })

    total_carbon = round(sum(d['total_carbon'] for d in plan) / 7, 2)
    total_cal    = round(sum(d['total_calories'] for d in plan) / 7, 0)

    # Swap suggestions — 3 lowest-carbon safe meals from lunch + dinner
    all_meals = safe_pool['lunch'] + safe_pool['dinner']
    all_meals.sort(key=lambda x: x['carbon'])
    swaps = all_meals[:3] if len(all_meals) > 3 else []

    return {
        'plan':               plan,
        'avg_daily_calories': total_cal,
        'avg_daily_carbon':   total_carbon,
        'target_calories':    round(target_cal),
        'bmr':                round(bmr),
        'swap_suggestions':   swaps,
        'carbon_label':       get_carbon_label(total_carbon)[0],
        'carbon_class':       get_carbon_label(total_carbon)[1],
        'user_allergies':     user_allergies,  # pass through for template info banner
    }