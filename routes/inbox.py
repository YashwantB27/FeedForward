from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from extensions import db
from models.models import Notification, Message, FoodListing
from models.user import User
from utils.notify import send_notification, notify_recipients_of_donation
from datetime import datetime

inbox = Blueprint('inbox', __name__, url_prefix='/inbox')


# ── Notification routes ───────────────────────────────────────────────────────

@inbox.route('/notifications')
@login_required
def notifications():
    notifs = Notification.query.filter_by(user_id=current_user.id)\
                               .order_by(Notification.created_at.desc()).limit(50).all()
    # Mark all as read
    Notification.query.filter_by(user_id=current_user.id, is_read=False).update({'is_read': True})
    db.session.commit()
    return render_template('inbox/notifications.html', notifs=notifs)

@inbox.route('/notifications/count')
@login_required
def notif_count():
    count       = Notification.query.filter_by(user_id=current_user.id, is_read=False).count()
    unread_msgs = Message.query.filter_by(receiver_id=current_user.id, is_read=False).count()
    return jsonify({'notifications': count, 'messages': unread_msgs, 'total': count + unread_msgs})

@inbox.route('/notifications/mark-read', methods=['POST'])
@login_required
def mark_notifs_read():
    Notification.query.filter_by(user_id=current_user.id, is_read=False).update({'is_read': True})
    db.session.commit()
    return jsonify({'ok': True})


# ── Message routes ────────────────────────────────────────────────────────────

@inbox.route('/messages')
@login_required
def messages():
    """Show all conversations (unique users messaged with)."""
    from sqlalchemy import or_
    sent     = Message.query.filter_by(sender_id=current_user.id).all()
    received = Message.query.filter_by(receiver_id=current_user.id).all()

    partner_ids = set()
    for m in sent:     partner_ids.add(m.receiver_id)
    for m in received: partner_ids.add(m.sender_id)

    conversations = []
    for pid in partner_ids:
        partner = User.query.get(pid)
        if not partner:
            continue
        last_msg = Message.query.filter(
            or_(
                (Message.sender_id == current_user.id) & (Message.receiver_id == pid),
                (Message.sender_id == pid) & (Message.receiver_id == current_user.id)
            )
        ).order_by(Message.created_at.desc()).first()

        unread = Message.query.filter_by(
            sender_id=pid, receiver_id=current_user.id, is_read=False
        ).count()

        conversations.append({
            'partner':  partner,
            'last_msg': last_msg,
            'unread':   unread,
        })

    conversations.sort(key=lambda c: c['last_msg'].created_at, reverse=True)
    return render_template('inbox/messages.html', conversations=conversations)


@inbox.route('/messages/<int:partner_id>', methods=['GET', 'POST'])
@login_required
def conversation(partner_id):
    """View and send messages in a conversation thread."""
    from sqlalchemy import or_
    partner    = User.query.get_or_404(partner_id)
    listing_id = request.args.get('listing_id', type=int)
    listing    = FoodListing.query.get(listing_id) if listing_id else None

    if request.method == 'POST':
        body = request.form.get('body', '').strip()
        if body:
            msg = Message(
                sender_id   = current_user.id,
                receiver_id = partner_id,
                listing_id  = listing_id,
                body        = body,
            )
            db.session.add(msg)

            # Notify the receiver
            send_notification(
                user_id = partner_id,
                type_   = 'message',
                title   = f'💬 New message from {current_user.name}',
                body    = body[:100] + ('…' if len(body) > 100 else ''),
                link    = url_for('inbox.conversation', partner_id=current_user.id)
            )
            db.session.commit()
        return redirect(url_for('inbox.conversation',
                                partner_id=partner_id,
                                listing_id=listing_id or ''))

    # Mark incoming messages as read
    Message.query.filter_by(
        sender_id=partner_id,
        receiver_id=current_user.id,
        is_read=False
    ).update({'is_read': True})
    db.session.commit()

    thread = Message.query.filter(
        or_(
            (Message.sender_id == current_user.id) & (Message.receiver_id == partner_id),
            (Message.sender_id == partner_id) & (Message.receiver_id == current_user.id)
        )
    ).order_by(Message.created_at.asc()).all()

    return render_template('inbox/conversation.html',
                           partner=partner, thread=thread,
                           listing=listing, listing_id=listing_id)


@inbox.route('/messages/send-ajax', methods=['POST'])
@login_required
def send_ajax():
    """AJAX endpoint for sending messages without page reload."""
    data       = request.get_json()
    partner_id = data.get('partner_id')
    body       = data.get('body', '').strip()
    listing_id = data.get('listing_id')

    if not body or not partner_id:
        return jsonify({'ok': False, 'msg': 'Missing fields'})

    msg = Message(
        sender_id   = current_user.id,
        receiver_id = partner_id,
        listing_id  = listing_id,
        body        = body,
    )
    db.session.add(msg)
    send_notification(
        user_id = partner_id,
        type_   = 'message',
        title   = f'💬 New message from {current_user.name}',
        body    = body[:100] + ('…' if len(body) > 100 else ''),
        link    = url_for('inbox.conversation', partner_id=current_user.id)
    )
    db.session.commit()

    return jsonify({
        'ok':       True,
        'id':       msg.id,
        'body':     msg.body,
        'time_ago': msg.time_ago,
        'sender':   current_user.name,
    })