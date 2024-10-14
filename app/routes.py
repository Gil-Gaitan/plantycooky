from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user # type: ignore
import sqlalchemy as sa # type: ignore
from app import db
from app.models import User
from flask_login import logout_user # type: ignore
from flask_login import login_required  # type: ignore
from flask import request
from urllib.parse import urlsplit

@app.route('/') # creates the route
@app.route('/index') # creates the index page
@login_required
def index():
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
    return render_template("index.html", title='Home Page', posts = posts) # renders the template

@app.route('/login', methods=['GET', 'POST']) # login route
def login():
    if current_user.is_authenticated: # checks if the user is already logged in
        return redirect(url_for('index')) # redirects the user to the index page
    form = LoginForm() # creates the form
    if form.validate_on_submit(): # checks if the form is valid
        user = db.session.scalar( 
            sa.select(User).where(User.username == form.username.data)) # checks if the user is in the database
        if user is None or not user.check_password(form.password.data): # checks if the user is not in the database or the password is incorrect
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data) # logs the user in
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
# flask run --port 5001