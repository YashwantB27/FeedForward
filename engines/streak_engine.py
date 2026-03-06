import os, base64, json, hashlib, requests
from datetime import datetime
from PIL import Image


def compute_phash(image_path, hash_size=16):
    try:
        img = Image.open(image_path).convert('L').resize(
            (hash_size * 4, hash_size * 4), Image.LANCZOS)
        pixels = list(img.getdata())
        avg = sum(pixels) / len(pixels)
        bits = ''.join('1' if p >= avg else '0' for p in pixels)
        return hex(int(bits, 2))[2:].zfill(hash_size * 4 // 4)
    except Exception:
        with open(image_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()


def is_duplicate_photo(hash1, hash2, threshold=10):
    try:
        xor = int(hash1, 16) ^ int(hash2, 16)
        return bin(xor).count('1') <= threshold
    except Exception:
        return False


def _image_to_b64(path):
    with open(path, 'rb') as f:
        return base64.standard_b64encode(f.read()).decode('utf-8')


def _media_type(path):
    ext = os.path.splitext(path)[1].lower()
    return {'.jpg': 'image/jpeg', '.jpeg': 'image/jpeg',
            '.png': 'image/png', '.webp': 'image/webp'}.get(ext, 'image/jpeg')


SYSTEM_PROMPT = """You are a fitness photo verifier for FeedForward.
Analyze the uploaded workout photo(s) and respond ONLY with valid JSON:
{
  "verdict": "approved" | "rejected" | "duplicate",
  "score": <0-100>,
  "feedback": "<1-2 sentence friendly message>",
  "is_fitness_photo": <true|false>,
  "change_detected": <true|false|null>
}
Rules:
- "duplicate": photos look nearly identical (same pose, background, lighting)
- "rejected": not a fitness/workout photo, or no effort shown
- "approved": genuine workout photo with visible effort or physical change
- Be encouraging but honest."""


def analyze_streak_photo(current_path, previous_path=None):
    api_key = os.environ.get('ANTHROPIC_API_KEY', '')
    if not api_key:
        return {'verdict': 'approved', 'score': 75.0,
                'feedback': 'Photo accepted (dev mode — no API key).',
                'is_fitness_photo': True, 'change_detected': True}

    content = []
    if previous_path and os.path.exists(previous_path):
        content.append({'type': 'text', 'text': 'Photo 2 (PREVIOUS — last week):'})
        content.append({'type': 'image', 'source': {
            'type': 'base64', 'media_type': _media_type(previous_path),
            'data': _image_to_b64(previous_path)}})
        content.append({'type': 'text', 'text': 'Photo 1 (CURRENT — this week):'})
    else:
        content.append({'type': 'text', 'text': 'Photo 1 (CURRENT — first submission):'})

    content.append({'type': 'image', 'source': {
        'type': 'base64', 'media_type': _media_type(current_path),
        'data': _image_to_b64(current_path)}})
    content.append({'type': 'text', 'text': 'Analyze and respond with JSON only.'})

    try:
        resp = requests.post(
            'https://api.anthropic.com/v1/messages',
            headers={'x-api-key': api_key, 'anthropic-version': '2023-06-01',
                     'content-type': 'application/json'},
            json={'model': 'claude-sonnet-4-20250514', 'max_tokens': 300,
                  'system': SYSTEM_PROMPT,
                  'messages': [{'role': 'user', 'content': content}]},
            timeout=30)
        resp.raise_for_status()
        raw = resp.json()['content'][0]['text'].strip()
        if raw.startswith('```'):
            raw = raw.split('```')[1]
            if raw.startswith('json'): raw = raw[4:]
        result = json.loads(raw)
        return {'verdict': result.get('verdict', 'rejected'),
                'score': float(result.get('score', 0)),
                'feedback': result.get('feedback', 'Unable to verify.'),
                'is_fitness_photo': result.get('is_fitness_photo', False),
                'change_detected': result.get('change_detected', None)}
    except Exception as e:
        return {'verdict': 'rejected', 'score': 0.0,
                'feedback': f'AI analysis failed. Please try again.',
                'is_fitness_photo': False, 'change_detected': None}


def get_current_streak(user_id):
    from models.streak_photo import StreakPhoto
    photos = (StreakPhoto.query
              .filter_by(user_id=user_id, ai_verdict='approved')
              .order_by(StreakPhoto.year.desc(), StreakPhoto.week_number.desc())
              .all())
    if not photos:
        return 0
    streak = 0
    now = datetime.utcnow()
    exp_week, exp_year = now.isocalendar()[1], now.year
    for p in photos:
        if p.week_number == exp_week and p.year == exp_year:
            streak += 1
            exp_week = exp_week - 1 if exp_week > 1 else 52
            if exp_week == 52: exp_year -= 1
        else:
            break
    return streak


def get_week_key():
    iso = datetime.utcnow().isocalendar()
    return iso[0], iso[1]