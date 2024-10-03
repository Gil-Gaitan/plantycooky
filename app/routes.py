from flask import render_template
from app import app
from app.forms import LoginForm

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

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

# flask run --port 5001