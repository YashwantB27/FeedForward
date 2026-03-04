from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from extensions import db
from models.models import ProgressLog, FoodListing
from models.user import User
from datetime import datetime, timedelta
import json

progress = Blueprint('progress', __name__, url_prefix='/progress')
admin    = Blueprint('admin', __name__, url_prefix='/admin')

# ── PROGRESS ─────────────────────────────────────────────────────────────────

@progress.route('/', methods=['GET','POST'])
@login_required
def index():
    if request.method == 'POST':
        today = datetime.utcnow().date()
        existing = ProgressLog.query.filter_by(user_id=current_user.id, log_date=today).first()
        data = dict(
            user_id=current_user.id,
            log_date=today,
            weight=float(request.form.get('weight') or 0),
            water_intake=float(request.form.get('water') or 0),
            calories_consumed=float(request.form.get('calories_consumed') or 0),
            calories_burned=float(request.form.get('calories_burned') or 0),
            workout_done=bool(request.form.get('workout_done')),
            mood=request.form.get('mood','good'),
            notes=request.form.get('notes','')
        )
        if existing:
            for k,v in data.items(): setattr(existing, k, v)
        else:
            db.session.add(ProgressLog(**data))
        db.session.commit()
        flash('Progress logged for today! 📊', 'success')
        return redirect(url_for('progress.index'))

    logs = ProgressLog.query.filter_by(user_id=current_user.id).order_by(ProgressLog.log_date.desc()).limit(30).all()
    today_log = ProgressLog.query.filter_by(user_id=current_user.id, log_date=datetime.utcnow().date()).first()

    # Build chart data
    dates   = [str(l.log_date) for l in reversed(logs)]
    weights = [l.weight or 0 for l in reversed(logs)]
    cal_in  = [l.calories_consumed or 0 for l in reversed(logs)]
    cal_out = [l.calories_burned or 0 for l in reversed(logs)]

    # Streak
    streak = 0
    for l in logs:
        if l.workout_done: streak += 1
        else: break

    chart_data = json.dumps({'dates':dates,'weights':weights,'cal_in':cal_in,'cal_out':cal_out})
    return render_template('progress/index.html', logs=logs, today_log=today_log, streak=streak, chart_data=chart_data)


# ── ADMIN ─────────────────────────────────────────────────────────────────────

def admin_required(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            flash('Admin access required.', 'danger')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated

@admin.route('/')
@login_required
@admin_required
def dashboard():
    total_users    = User.query.count()
    total_listings = FoodListing.query.count()
    total_claimed  = FoodListing.query.filter_by(status='claimed').count()
    total_active   = FoodListing.query.filter_by(status='available').count()
    recent_users   = User.query.order_by(User.created_at.desc()).limit(10).all()
    recent_food    = FoodListing.query.order_by(FoodListing.posted_at.desc()).limit(10).all()
    stats = {
        'users': total_users,
        'listings': total_listings,
        'claimed': total_claimed,
        'active': total_active,
        'kg_saved': total_claimed * 2,
        'meals': total_claimed
    }
    return render_template('admin/dashboard.html', stats=stats, recent_users=recent_users, recent_food=recent_food)

@admin.route('/users')
@login_required
@admin_required
def users():
    all_users = User.query.order_by(User.created_at.desc()).all()
    return render_template('admin/users.html', users=all_users)

@admin.route('/listings')
@login_required
@admin_required
def listings():
    all_listings = FoodListing.query.order_by(FoodListing.posted_at.desc()).all()
    return render_template('admin/listings.html', listings=all_listings)

@admin.route('/delete-listing/<int:lid>')
@login_required
@admin_required
def delete_listing(lid):
    l = FoodListing.query.get_or_404(lid)
    db.session.delete(l)
    db.session.commit()
    flash('Listing removed.', 'info')
    return redirect(url_for('admin.listings'))

@admin.route('/make-admin/<int:uid>')
@login_required
@admin_required
def make_admin(uid):
    u = User.query.get_or_404(uid)
    u.role = 'admin'
    db.session.commit()
    flash(f'{u.name} is now an admin.', 'success')
    return redirect(url_for('admin.users'))
