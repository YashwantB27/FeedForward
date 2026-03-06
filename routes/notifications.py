from flask import Blueprint, jsonify, render_template
from flask_login import login_required, current_user
from extensions import db
from models.notification import Notification

notifications = Blueprint('notifications', __name__)

# Get all notifications for current user
@notifications.route('/notifications')
@login_required
def get_notifications():
    notifs = Notification.query.filter_by(user_id=current_user.id)\
             .order_by(Notification.created_at.desc()).limit(20).all()
    return render_template('notifications.html', notifications=notifs)

# Get unread count (for bell icon badge)
@notifications.route('/notifications/unread-count')
@login_required
def unread_count():
    count = Notification.query.filter_by(
        user_id=current_user.id, is_read=False
    ).count()
    return jsonify({'count': count})

# Mark all as read
@notifications.route('/notifications/mark-read', methods=['POST'])
@login_required
def mark_all_read():
    Notification.query.filter_by(
        user_id=current_user.id, is_read=False
    ).update({'is_read': True})
    db.session.commit()
    return jsonify({'success': True})

# Mark single notification as read
@notifications.route('/notifications/mark-read/<int:notif_id>', methods=['POST'])
@login_required
def mark_one_read(notif_id):
    notif = Notification.query.get_or_404(notif_id)
    if notif.user_id == current_user.id:
        notif.is_read = True
        db.session.commit()
    return jsonify({'success': True})