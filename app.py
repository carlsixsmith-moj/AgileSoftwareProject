import sys
import os

# add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, redirect, url_for
from flask_login import LoginManager

from controllers import *
from models import db, User

# -- Create the flask application --
app = Flask(__name__)

# -- Configure the database --
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# -- initialise the database with the app --
db.init_app(app)

# -- Set up Flask-Login --
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'warning'

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

app.register_blueprint(participants_bp)
app.register_blueprint(assessments_bp)
app.register_blueprint(auth_bp)

with app.app_context():
    from seed import seed_database
    seed_database()


@app.route('/')
def home():
    return redirect(url_for('participants.list_participants'))

if __name__ == '__main__':
    app.run(debug=True)