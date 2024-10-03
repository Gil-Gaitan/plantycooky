from flask import Flask
from config import Config 
#import the Config class from config.py

# Create an instance of the Flask class
app = Flask(__name__)
# Load the configuration
app.config.from_object(Config)

from app import routes
