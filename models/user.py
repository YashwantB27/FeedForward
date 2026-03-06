from extensions import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(100), nullable=False)
    email         = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role          = db.Column(db.String(20), default='user')  # user / donor / recipient / admin

    # Profile
    age           = db.Column(db.Integer)
    weight        = db.Column(db.Float)
    height        = db.Column(db.Float)
    gender        = db.Column(db.String(10))
    dietary_pref  = db.Column(db.String(20))   # veg / non_veg / vegan
    health_goal   = db.Column(db.String(20))   # lose_weight / gain_muscle / stay_fit
    fitness_level = db.Column(db.String(20))   # beginner / intermediate / advanced
    equipment     = db.Column(db.String(20))   # none / dumbbells / gym
    days_per_week = db.Column(db.Integer, default=4)
    location      = db.Column(db.String(200))
    latitude      = db.Column(db.Float)
    longitude     = db.Column(db.Float)
    profile_complete = db.Column(db.Boolean, default=False)
    allergies     = db.Column(db.String(200), default='')  # comma-separated e.g. "gluten,dairy,nuts"
    created_at    = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    meal_plans    = db.relationship('MealPlan',     backref='user', lazy=True)
    exercise_plans= db.relationship('ExercisePlan', backref='user', lazy=True)
    donations     = db.relationship('FoodListing',  foreign_keys='FoodListing.donor_id',    backref='donor',     lazy=True)
    claims        = db.relationship('FoodListing',  foreign_keys='FoodListing.claimed_by',  backref='recipient', lazy=True)
    progress_logs = db.relationship('ProgressLog',  backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.name}>"