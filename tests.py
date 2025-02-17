import os  # Import the os module for environment variable handling

# Set the database URL to use an in-memory SQLite database for testing
os.environ["DATABASE_URL"] = "sqlite://"

from datetime import datetime, timezone, timedelta
import unittest  # Import unittest for unit testing
from app import app, db  # Import the Flask app and database
from app.models import User, Post  # Import the User and Post models


# Unit tests for the User model
class UserModelCase(unittest.TestCase):
    def setUp(self):
        # Create a new app context and initialize the test database
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        # Remove the session, drop all tables, and pop the app context
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        # Test password hashing and verification
        u = User(username="susan", email="susan@example.com")
        u.set_password("cat")
        self.assertFalse(u.check_password("dog"))  # Wrong password
        self.assertTrue(u.check_password("cat"))  # Correct password

    def test_avatar(self):
        # Test the avatar URL generation based on the email hash
        u = User(username="john", email="john@example.com")
        self.assertEqual(
            u.avatar(128),
            (
                "https://www.gravatar.com/avatar/"
                "d4c74594d841139328695756648b6bd6"
                "?d=identicon&s=128"
            ),
        )

    def test_follow(self):
        # Test user following and unfollowing functionality
        u1 = User(username="john", email="john@example.com")
        u2 = User(username="susan", email="susan@example.com")
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        # Verify initial follow state (both should have no followers)
        following = db.session.scalars(u1.following.select()).all()
        followers = db.session.scalars(u2.followers.select()).all()
        self.assertEqual(following, [])
        self.assertEqual(followers, [])

        # u1 follows u2
        u1.follow(u2)
        db.session.commit()
        self.assertTrue(u1.is_following(u2))
        self.assertEqual(u1.following_count(), 1)
        self.assertEqual(u2.followers_count(), 1)

        # Verify the follow relationship
        u1_following = db.session.scalars(u1.following.select()).all()
        u2_followers = db.session.scalars(u2.followers.select()).all()
        self.assertEqual(u1_following[0].username, "susan")
        self.assertEqual(u2_followers[0].username, "john")

        # u1 unfollows u2
        u1.unfollow(u2)
        db.session.commit()
        self.assertFalse(u1.is_following(u2))
        self.assertEqual(u1.following_count(), 0)
        self.assertEqual(u2.followers_count(), 0)

    def test_follow_posts(self):
        # Test posts appearing in the feed based on follow relationships

        # Create four users
        u1 = User(username="john", email="john@example.com")
        u2 = User(username="susan", email="susan@example.com")
        u3 = User(username="mary", email="mary@example.com")
        u4 = User(username="david", email="david@example.com")
        db.session.add_all([u1, u2, u3, u4])

        # Create four posts with timestamps
        now = datetime.now(timezone.utc)
        p1 = Post(
            body="post from john", author=u1, timestamp=now + timedelta(seconds=1)
        )
        p2 = Post(
            body="post from susan", author=u2, timestamp=now + timedelta(seconds=4)
        )
        p3 = Post(
            body="post from mary", author=u3, timestamp=now + timedelta(seconds=3)
        )
        p4 = Post(
            body="post from david", author=u4, timestamp=now + timedelta(seconds=2)
        )
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

        # Set up follow relationships
        u1.follow(u2)  # John follows Susan
        u1.follow(u4)  # John follows David
        u2.follow(u3)  # Susan follows Mary
        u3.follow(u4)  # Mary follows David
        db.session.commit()

        # Fetch and check following posts for each user
        f1 = db.session.scalars(
            u1.following_posts()
        ).all()  # John should see Susan & David's posts
        f2 = db.session.scalars(
            u2.following_posts()
        ).all()  # Susan should see Mary's posts
        f3 = db.session.scalars(
            u3.following_posts()
        ).all()  # Mary should see David's posts
        f4 = db.session.scalars(u4.following_posts()).all()  # David follows no one

        self.assertEqual(
            f1, [p2, p4, p1]
        )  # John's feed should have Susan, David, and his own post
        self.assertEqual(
            f2, [p2, p3]
        )  # Susan's feed should have her own and Mary's post
        self.assertEqual(
            f3, [p3, p4]
        )  # Mary's feed should have her own and David's post
        self.assertEqual(f4, [p4])  # David should only see his own post


# Run the tests when the script is executed
if __name__ == "__main__":
    unittest.main(verbosity=2)
