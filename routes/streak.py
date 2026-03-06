import os
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from extensions import db
from models.streak_photo import StreakPhoto
from engines.streak_engine import (compute_phash, is_duplicate_photo,
                                   analyze_streak_photo, get_current_streak, get_week_key)
from werkzeug.utils import secure_filename

streak_bp = Blueprint('streak', __name__, url_prefix='/streak')

UPLOAD_FOLDER = os.path.join('static', 'streak_photos')
ALLOWED_EXT   = {'jpg', 'jpeg', 'png', 'webp'}


def _allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT


def _save(file, user_id, week, year):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    ext  = file.filename.rsplit('.', 1)[1].lower()
    name = secure_filename(f"streak_{user_id}_{year}_w{week}.{ext}")
    path = os.path.join(UPLOAD_FOLDER, name)
    file.save(path)
    return path


@streak_bp.route('/')
@login_required
def index():
    year, week    = get_week_key()
    current_streak = get_current_streak(current_user.id)
    this_week     = StreakPhoto.query.filter_by(
        user_id=current_user.id, year=year, week_number=week).first()
    history       = (StreakPhoto.query.filter_by(user_id=current_user.id)
                     .order_by(StreakPhoto.year.desc(), StreakPhoto.week_number.desc())
                     .limit(12).all())
    return render_template('streak/index.html', current_streak=current_streak,
                           this_week=this_week, history=history, week=week, year=year)


@streak_bp.route('/upload', methods=['POST'])
@login_required
def upload():
    year, week = get_week_key()

    if StreakPhoto.query.filter_by(user_id=current_user.id, year=year, week_number=week).first():
        flash('Already submitted this week! Come back next week. 📅', 'info')
        return redirect(url_for('streak.index'))

    if 'photo' not in request.files or not request.files['photo'].filename:
        flash('Please select a photo.', 'danger')
        return redirect(url_for('streak.index'))

    file = request.files['photo']
    if not _allowed(file.filename):
        flash('Only JPG, PNG or WebP images accepted.', 'danger')
        return redirect(url_for('streak.index'))

    photo_path = _save(file, current_user.id, week, year)
    curr_hash  = compute_phash(photo_path)

    prev_week   = week - 1 if week > 1 else 52
    prev_year   = year if week > 1 else year - 1
    prev_record = StreakPhoto.query.filter_by(
        user_id=current_user.id, year=prev_year, week_number=prev_week).first()

    # Layer 1: pixel-level duplicate check
    if prev_record and is_duplicate_photo(curr_hash, prev_record.photo_hash):
        db.session.add(StreakPhoto(
            user_id=current_user.id, photo_path=photo_path, photo_hash=curr_hash,
            week_number=week, year=year, ai_verdict='duplicate',
            ai_feedback="Looks identical to last week's photo. Upload a new one!",
            ai_score=0.0, streak_count=0))
        db.session.commit()
        flash('📸 Duplicate detected! Upload a fresh workout photo.', 'warning')
        return redirect(url_for('streak.index'))

    # Layer 2: Claude AI vision analysis
    prev_path = prev_record.photo_path if prev_record and os.path.exists(prev_record.photo_path or '') else None
    result    = analyze_streak_photo(photo_path, prev_path)

    current_streak = get_current_streak(current_user.id)
    new_streak     = current_streak + 1 if result['verdict'] == 'approved' else 0

    db.session.add(StreakPhoto(
        user_id=current_user.id, photo_path=photo_path, photo_hash=curr_hash,
        week_number=week, year=year, ai_verdict=result['verdict'],
        ai_feedback=result['feedback'], ai_score=result['score'],
        streak_count=new_streak))
    db.session.commit()

    if result['verdict'] == 'approved':
        flash(f'🔥 Streak verified! {new_streak}-week streak! {result["feedback"]}', 'success')
    elif result['verdict'] == 'duplicate':
        flash(f'📸 Duplicate photo! {result["feedback"]}', 'warning')
    else:
        flash(f'❌ Not accepted. {result["feedback"]}', 'danger')

    return redirect(url_for('streak.index'))