# MAIN.md - Branch Development Documentation

## 02/13/25 - Kickstarting it Back Up

### Instructions to Run:

1. **Activate Virtual Environment:**
   ```bash
   source venv/bin/activate
   ```

2. **Run the Application:**
   ```bash
   flask run --port 5001
   ```

### Database Configuration:

- **Database**: Flask-SQLAlchemy, Flask-Migrate  
- **User Model Fields**: `id`, `username`, `email`, `password_hash` (defined in `app/models.py`)

### Accessing and Reading Data:

**Note:** Virtual environment setup was adjusted to ensure smooth Python execution.

1. **Setting up the App Context:**
   ```python
   >>> from app import app, db
   >>> from app.models import User, Post
   >>> import sqlalchemy as sa
   >>> app.app_context().push()
   ```

2. **Querying Data:**
   ```python
   query = sa.select(User)
   users = db.session.scalars(query).all()
   print(users)
   ```

---

Will get to the email process next time

---

## 11/05/24 - Postmark Feature

- **Postmark Setup:**
   - Signed up for Postmark service.
   - Basic instructions can be found in settings. Login credentials are saved in cloud storage.
   - The service allows up to 100 emails per day (limited to the PSC domain).
   - To send emails to other domains, authentication requests can be made.
   - **Important**: Check the "Default Broadcast Stream" settings.

- **Issue**: Unsuccessful in sending an email.

---

## 10/02/24 - WTForms for Login (Chapter 3)

- Completed the login form.
- Adjustments needed for proper links and redirects.

---

## 10/13/23 - Preparing the User Model for Flask-Login

### The Four Required Flask-Login Methods for User Model:

1. **`is_authenticated`**:  
   Returns `True` if the user has valid credentials, otherwise `False`.

2. **`is_active`**:  
   Returns `True` if the user’s account is active, otherwise `False`.

3. **`is_anonymous`**:  
   Returns `False` for regular users and `True` only for a special, anonymous user.

4. **`get_id()`**:  
   Returns a unique identifier for the user as a string.

---

## 10/16/24 - Changing Posts Per Page

- The configuration for adjusting the number of posts per page is located in the config file.

---

## app/models.py - Database Model Representations

Example of adding a relation between users (e.g., followers):

```python
followers = sa.Table(
    'followers',
    db.metadata,
    sa.Column('follower_id', sa.Integer, sa.ForeignKey('user.id'), primary_key=True),
    sa.Column('followed_id', sa.Integer, sa.ForeignKey('user.id'), primary_key=True)
)
```

### Flask Commands:

1. **Activate Virtual Environment:**
   ```bash
   source venv/bin/activate
   ```

2. **Run the Flask Application:**
   ```bash
   flask run --port 5001
   ```

3. **Initialize Database:**
   ```bash
   flask db init
   flask db migrate -m "Create users table"
   ```

4. **Query Data:**
   ```python
   >>> from app import app, db
   >>> from app.models import User, Post
   >>> import sqlalchemy as sa
   >>> app.app_context().push()
   ```

---