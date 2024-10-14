from flask import Flask 
from config import Config #import the Config class from config.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__) # Create an instance of the Flask class
app.config.from_object(Config)# Load the configuration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

# Flask-SQLAlchemy and Flask-Migrate initialization