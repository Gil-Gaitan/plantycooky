from flask import render_template, flash, redirect, url_for
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

@app.route('/login', methods=['GET', 'POST']) # login route
def login():
    form = LoginForm()
    if form.validate_on_submit(): # checks if the form is valid
        flash('Login requested for user {}, remember_me={}'.format( # flashes a message to the user
            form.username.data, form.remember_me.data)) # flashes a message to the user
        return redirect(url_for('index')) # redirects the user to the index page
    return render_template('login.html', title='Sign In', form=form) # renders the template

# flask run --port 5001