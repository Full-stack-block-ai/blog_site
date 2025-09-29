from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


# Initialize Flask app
app = Flask(__name__)
# Apply config from Config class
app.config.from_object(Config)
# Set up SQLAlchemy with app
db = SQLAlchemy(app)
# Set up Migrate with app and db
migrate = Migrate(app, db)
# setuplogin manager
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models

