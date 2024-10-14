MAIN.md documents branch development

10/2/24 CH3 WTForms for login
    login form is complete
    adjust for proper links and redirects

10/13/23 

use:
source venv/bin/activate
flask run --port 5001

flask db init
flask db migrate -m "users table"

>>> from app import app, db
>>> from app.models import User, Post
>>> import sqlalchemy as sa
>>> app.app_context().push()
