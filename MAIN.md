# MAIN.md Documentation for Branch Development

## 11/05/24 - Postmark Feature
- Signed up for postmark. 
      - There are basic instructions in settings. Login info saved in cloud note.
      - May send up to 100 emails a day. Can only send emails to the PSC domain.
      - May request authentication to send to more email addresses.
      - Settings for server, look for "Default Broadcast Stream"

      UNSUCCESSFUL in sending an email

---

## 10/02/24 - CH3 WTForms for Login
- Login form is complete
- Adjust for proper links and redirect

---

## 10/13/23 - Preparing The User Model for Flask-Login

The four required items for Flask-Login are listed below:

1. **`is_authenticated`**:  
   A property that is `True` if the user has valid credentials, or `False` otherwise.
   
2. **`is_active`**:  
   A property that is `True` if the user's account is active, or `False` otherwise.
   
3. **`is_anonymous`**:  
   A property that is `False` for regular users and `True` only for a special, anonymous user.
   
4. **`get_id()`**:  
   A method that returns a unique identifier for the user as a string.

---

10/16/24 - to change posts per page, the variable is in config file. 

## app/models.py - Database Model Representations

Example of adding a relation:

```python
followers = sa.Table(
    'followers',
    db.metadata,
    sa.Column('follower_id', sa.Integer, sa.ForeignKey('user.id'), primary_key=True),
    sa.Column('followed_id', sa.Integer, sa.ForeignKey('user.id'), primary_key=True)
)

source venv/bin/activate
flask run --port 5001

flask db init
flask db migrate -m "users table"

>>> from app import app, db
>>> from app.models import User, Post
>>> import sqlalchemy as sa
>>> app.app_context().push()