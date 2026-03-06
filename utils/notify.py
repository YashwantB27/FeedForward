from extensions import db
from models.models import Notification


def send_notification(user_id, type_, title, body, link=''):
    """Helper to create a notification for any user."""
    notif = Notification(
        user_id = user_id,
        type    = type_,
        title   = title,
        body    = body,
        link    = link
    )
    db.session.add(notif)
    # Don't commit here — let the caller commit


def notify_recipients_of_donation(listing):
    """Notify all recipient/user roles about a new food donation."""
    from models.user import User
    from flask import url_for

    recipients = User.query.filter(
        User.role.in_(['recipient', 'user']),
        User.id != listing.donor_id
    ).all()

    for r in recipients:
        send_notification(
            user_id = r.id,
            type_   = 'new_donation',
            title   = '🍱 New Food Available!',
            body    = f'{listing.food_name} ({listing.quantity}) is available at {listing.location}.',
            link    = url_for('foodbank.index')
        )