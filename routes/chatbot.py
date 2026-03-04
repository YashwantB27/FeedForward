from flask import Blueprint, render_template, request, jsonify, session
from flask_login import login_required, current_user
import os, json

chatbot = Blueprint('chatbot', __name__, url_prefix='/chatbot')

SYSTEM_PROMPT = """You are FeedGenie, a friendly and knowledgeable AI health assistant for the FeedForward platform.

FeedForward is a health & sustainability app that provides:
- Personalized 7-day AI meal plans based on user's dietary preferences, goals and calorie needs
- AI exercise plans tailored to fitness level and goals
- Carbon footprint tracking for food choices
- Food bank listings to donate and claim surplus food
- Progress tracking (weight, water, calories, workouts)
- NutriBot and calorie calculator features

Your role is to:
- Answer questions about nutrition, diet, fitness, and healthy living
- Help users understand their meal and exercise plans
- Give advice on food choices, carbon footprint, and sustainability
- Guide users on how to use FeedForward features
- Suggest healthy Indian and international food options
- Answer questions about calories, macros, BMI, water intake

Keep responses concise, warm, and practical. Use emojis occasionally to be friendly.
Always stay on topic — health, nutrition, fitness, and the FeedForward platform.
If asked something completely unrelated, politely redirect to health topics.
Never give medical diagnoses. Always recommend consulting a doctor for medical issues."""


@chatbot.route('/')
@login_required
def index():
    return render_template('chatbot.html')


@chatbot.route('/ask', methods=['POST'])
@login_required
def ask():
    data     = request.get_json()
    messages = data.get('messages', [])

    if not messages:
        return jsonify({'ok': False, 'msg': 'No messages provided'})

    # Build user context
    user_context = f"""Current user profile:
- Name: {current_user.name}
- Age: {getattr(current_user, 'age', 'unknown')}
- Weight: {getattr(current_user, 'weight', 'unknown')} kg
- Height: {getattr(current_user, 'height', 'unknown')} cm
- Gender: {getattr(current_user, 'gender', 'unknown')}
- Dietary preference: {getattr(current_user, 'dietary_pref', 'unknown')}
- Health goal: {getattr(current_user, 'health_goal', 'unknown')}
- Fitness level: {getattr(current_user, 'fitness_level', 'unknown')}"""

    full_system = SYSTEM_PROMPT + "\n\n" + user_context

    try:
        import urllib.request
        payload = json.dumps({
            "model": "claude-sonnet-4-20250514",
            "max_tokens": 1000,
            "system": full_system,
            "messages": messages
        }).encode('utf-8')

        req = urllib.request.Request(
            'https://api.anthropic.com/v1/messages',
            data=payload,
            headers={
                'Content-Type':      'application/json',
                'anthropic-version': '2023-06-01',
            },
            method='POST'
        )

        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read().decode('utf-8'))
            reply  = result['content'][0]['text']
            return jsonify({'ok': True, 'reply': reply})

    except Exception as e:
        return jsonify({'ok': False, 'msg': str(e)})