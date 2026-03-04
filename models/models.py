from extensions import db
from datetime import datetime

class MealPlan(db.Model):
    __tablename__ = 'meal_plans'
    id             = db.Column(db.Integer, primary_key=True)
    user_id        = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    plan_json      = db.Column(db.Text, nullable=False)
    total_calories = db.Column(db.Float)
    carbon_score   = db.Column(db.Float)
    week_number    = db.Column(db.Integer, default=1)
    created_at     = db.Column(db.DateTime, default=datetime.utcnow)

class ExercisePlan(db.Model):
    __tablename__ = 'exercise_plans'
    id             = db.Column(db.Integer, primary_key=True)
    user_id        = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    plan_json      = db.Column(db.Text, nullable=False)
    fitness_goal   = db.Column(db.String(30))
    fitness_level  = db.Column(db.String(20))
    days_per_week  = db.Column(db.Integer)
    created_at     = db.Column(db.DateTime, default=datetime.utcnow)

class FoodListing(db.Model):
    __tablename__ = 'food_listings'
    id           = db.Column(db.Integer, primary_key=True)
    donor_id     = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    food_name    = db.Column(db.String(100), nullable=False)
    category     = db.Column(db.String(50))
    quantity     = db.Column(db.String(50))
    expiry_date  = db.Column(db.DateTime)
    location     = db.Column(db.String(200))
    latitude     = db.Column(db.Float, default=17.3850)
    longitude    = db.Column(db.Float, default=78.4867)
    photo_url    = db.Column(db.String(300))
    description  = db.Column(db.Text)
    status       = db.Column(db.String(20), default='available')  # available/claimed/picked_up/expired
    claimed_by   = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    claimed_at   = db.Column(db.DateTime)
    picked_up_at = db.Column(db.DateTime)
    posted_at    = db.Column(db.DateTime, default=datetime.utcnow)
    donor_rating = db.Column(db.Float)        # avg rating from recipients
    allergens    = db.Column(db.String(200))  # comma-separated

    @property
    def is_expired(self):
        return self.expiry_date and datetime.utcnow() > self.expiry_date

    @property
    def hours_to_expiry(self):
        if self.expiry_date:
            delta = self.expiry_date - datetime.utcnow()
            return max(0, int(delta.total_seconds() / 3600))
        return None

class ProgressLog(db.Model):
    __tablename__ = 'progress_logs'
    id                = db.Column(db.Integer, primary_key=True)
    user_id           = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    log_date          = db.Column(db.Date, default=datetime.utcnow().date)
    weight            = db.Column(db.Float)
    water_intake      = db.Column(db.Float, default=0)
    calories_consumed = db.Column(db.Float, default=0)
    calories_burned   = db.Column(db.Float, default=0)
    workout_done      = db.Column(db.Boolean, default=False)
    steps             = db.Column(db.Integer, default=0)
    mood              = db.Column(db.String(20))
    notes             = db.Column(db.Text)
    created_at        = db.Column(db.DateTime, default=datetime.utcnow)

class CustomWorkout(db.Model):
    """User-built custom workout routines"""
    __tablename__ = 'custom_workouts'
    id          = db.Column(db.Integer, primary_key=True)
    user_id     = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name        = db.Column(db.String(100), nullable=False)
    exercises   = db.Column(db.Text)   # JSON list of exercises
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)

class DonorRating(db.Model):
    """Recipient ratings for donors"""
    __tablename__ = 'donor_ratings'
    id          = db.Column(db.Integer, primary_key=True)
    listing_id  = db.Column(db.Integer, db.ForeignKey('food_listings.id'))
    donor_id    = db.Column(db.Integer, db.ForeignKey('users.id'))
    rater_id    = db.Column(db.Integer, db.ForeignKey('users.id'))
    rating      = db.Column(db.Integer)   # 1-5
    comment     = db.Column(db.String(300))
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)

class Badge(db.Model):
    __tablename__ = 'badges'
    id         = db.Column(db.Integer, primary_key=True)
    user_id    = db.Column(db.Integer, db.ForeignKey('users.id'))
    badge_key  = db.Column(db.String(50))
    earned_at  = db.Column(db.DateTime, default=datetime.utcnow)
