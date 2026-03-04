from flask import Flask, session
from extensions import db, login_manager, bcrypt
from models.user import User
from translations import get_translations
import json, os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']                     = os.environ.get('SECRET_KEY', 'feedforward_local_2025')
    app.config['SQLALCHEMY_DATABASE_URI']        = 'sqlite:///feedforward.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER']                  = 'static/uploads'
    app.config['MAX_CONTENT_LENGTH']             = 5 * 1024 * 1024
    app.config['WTF_CSRF_ENABLED']               = False

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    login_manager.login_view             = 'auth.login'
    login_manager.login_message          = 'Please login to access this page.'
    login_manager.login_message_category = 'info'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Inject translations + lang into every template automatically
    @app.context_processor
    def inject_globals():
        lang_code = session.get('lang', 'en')
        return {'t': get_translations(lang_code), 'lang': lang_code}

    # fromjson filter for templates
    @app.template_filter('fromjson')
    def fromjson_filter(s):
        try:
            return json.loads(s)
        except Exception:
            return []

    # Register blueprints
    from routes.auth           import auth
    from routes.main           import main
    from routes.diet           import diet
    from routes.exercise       import exercise
    from routes.foodbank       import foodbank
    from routes.progress_admin import progress, admin
    from routes.lang           import lang as lang_bp
    from routes.chatbot        import chatbot

    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(diet)
    app.register_blueprint(exercise)
    app.register_blueprint(foodbank)
    app.register_blueprint(progress)
    app.register_blueprint(admin)
    app.register_blueprint(lang_bp)
    app.register_blueprint(chatbot)

    # Create all DB tables
    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
