import sys
import os

# add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask

from controllers import participants_bp
from models import db

# -- Create the flask application --
app = Flask(__name__)

# -- Configure the database --
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# -- initialise the database with the app --
db.init_app(app)
app.register_blueprint(participants_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)