from flask import render_template
from app import app
# first view function for this application

@app.route('/') # creates the route
@app.route('/index') # creates the index page
def index():
    user = {'username': 'Seed Master'} # fake user
    posts = [
        {
            'author': {'username': 'Johnny Apple'},
            'body': 'The seed is the beginning of solution.'
        },
        {
            'author': {'username': 'AlwayzCookin'},
            'body': 'Made a delicious program today!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts = posts) # renders the template
# flask run --port 5001