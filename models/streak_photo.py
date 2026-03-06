from extensions import db
from datetime import datetime

class StreakPhoto(db.Model):
    __tablename__ = 'streak_photos'

    id           = db.Column(db.Integer, primary_key=True)
    user_id      = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    photo_path   = db.Column(db.String(300), nullable=False)
    photo_hash   = db.Column(db.String(64),  nullable=False)
    week_number  = db.Column(db.Integer, nullable=False)
    year         = db.Column(db.Integer, nullable=False)
    ai_verdict   = db.Column(db.String(20), default='pending')  # pending/approved/rejected/duplicate
    ai_feedback  = db.Column(db.Text)
    ai_score     = db.Column(db.Float)
    streak_count = db.Column(db.Integer, default=0)
    uploaded_at  = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('streak_photos', lazy=True))