MAIN.md documents branch development

10/2/24 CH3 WTForms for login
    login form is complete
    adjust for proper links and redirects

10/13/23 Preparing The User Model for Flask-Login
The four required items are listed below:
    is_authenticated: a property that is True if the user has valid credentials or False otherwise.
    is_active: a property that is True if the user's account is active or False otherwise.
    is_anonymous: a property that is False for regular users, and True only for a special, anonymous user.
    get_id(): a method that returns a unique identifier for the user as a string.

use:
source venv/bin/activate
flask run --port 5001

flask db init
flask db migrate -m "users table"

>>> from app import app, db
>>> from app.models import User, Post
>>> import sqlalchemy as sa
>>> app.app_context().push()
