from flask import Flask

app = Flask(__name__) # Create an instance of the Flask class

from app import routes # Import the routes module, doesn't exist yet.
