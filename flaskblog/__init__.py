"""
step1i)
to create the flask page import flask (Flask=a web framework)
flask library was installed in the command line/computer terminal (cmd) first
"""
from flask import Flask

#to create database: pip install flask-SQLAlchemy in cmd first
from flask_sqlalchemy import SQLAlchemy

"""Flask-Bcrypt is a Flask extension that provides bcrypt hashing utilities:
to protect passwords for instance
Then below add 'Bcrypt=... ' to initialise it in the app; then go to route.py
"""
from flask_bcrypt import Bcrypt

"""
pip install flask-login in cmd
then import LoginManager
"Flask-Login provides user session management for Flask. 
It handles the common tasks of logging in, logging out, 
and remembering your users’ sessions over extended periods of time."[Flask Login Documentation: https://flask-login.readthedocs.io/en/latest/]
"""
from flask_login import LoginManager

"""set up the application/Create an instance. 
Python assigns the name "__main__" to the script when the script is executed. 
"""
app = Flask(__name__)

"""
Create a key for deployment/to protect your app.
In the IDLE Python, type the two lines below
>>> import secrets
>>> secrets.token_hex(16)
16=bytes
Random string received=
'dde4956d1fd2454b7a3fa4035a9135f8'
"""
app.config['SECRET_KEY'] = 'dde4956d1fd2454b7a3fa4035a9135f8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
"""view is the function name of our route - pass on to urlfor function"""
login_manager.login_view = 'login'
"""to have a nice message for login>see bootstrap"""
login_manager.login_message_category = 'info'

#circular import errors, so write here the import

from flaskblog import routes