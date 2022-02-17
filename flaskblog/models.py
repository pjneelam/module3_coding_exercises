"""
step 4
See comments in flask_server.py, renamed __init__.py

create a model/class
class Repository - import from db.Model:
passwords etc will be hashed so length=60
"""
#import datetime for dates to appear on posts
from datetime import datetime

"""
To reduce circular import errors, the files were cleaned, and instead of putting all 
the codes in one file (initially flask_server file, it was broken)
"""


from flaskblog import db, login_manager

"""
Flask-login requires a User model with the following properties:
has an is_authenticated() method that returns True if the user has provided valid credentials
has an is_active() method that returns True if the user’s account is active
has an is_anonymous() method that returns True if the current user is an anonymous user
has a get_id() method which, given a User instance, returns the unique ID for that object
UserMixin class provides the implementation of this properties. 
It's the reason you can call for example is_authenticated to check if login credentials provided is correct or not 
instead of having to write a method to do that yourself. [https://stackoverflow.com/questions/63231163/what-is-the-usermixin-in-flask]
"""

from flask_login import UserMixin

"""
create a function with a decorator (user_loader):
for reloading the user from the user id stored in the session (check documentation - extensions)
@ symbols: specifies a decorator
"""
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    #add columns for this table
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    #one-to-many relation: one user can have many posts (to link user to post); lazy=loading of data in one go
    posts = db.relationship('Post', backref='author', lazy=True)
    #for the printing of info
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

