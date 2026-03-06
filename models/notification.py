from extensions import db
from datetime import datetime

class Notification(db.Model):
    __tablename__ = 'notifications'

    id         = db.Column(db.Integer, primary_key=True)
    user_id    = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title      = db.Column(db.String(100), nullable=False)
    message    = db.Column(db.String(255), nullable=False)
    type       = db.Column(db.String(50))   # 'donation', 'claim', 'message', 'reminder'
    is_read    = db.Column(db.Boolean, default=False)
    link       = db.Column(db.String(200))  # optional redirect URL
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref='notifications')