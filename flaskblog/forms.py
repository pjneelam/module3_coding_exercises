"""
step 3: for users to be able to create accounts, login etc
instead of creating your own forms
import flask extensions to create the form: wtf=extension
validators: to have input fields in the form+validate the content of those fields once submitted
InputRequired=for users to be able to sign up/in; Length=no of characters for password; EqualTo=compares two fields
"""

from flask_wtf import FlaskForm
from flaskblog.forms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

# create Registration form class, which inherits from FlaskForm
class RegistrationForm(FlaskForm):
#create attributes: username etc.
#add validators, which we have imported from wtforms. E.g limit no of characters for the username etc.
    username = StringField('username', validators=[DataRequired(),Length(min=2, max=20)])
    email=StringField('email', validators=[DataRequired(),Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password',validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField('sign up')

"""
create custom validation (by creating a function) for registration to the form. 
Can also add some validation checks (to know if email/user exists in the database) in the routes
But choice= do it here: gets checked when form is validated
check wtforms documentation: https://wtforms.readthedocs.io/en/3.0.x/

Explaining steps below:
def validate_username()
username=the field we want to validate
if user is True/that is exists, then validation error is raised, and message is between brackets
users must be imported from models.py - import users - go up
user=User.query : to know if the user comes from our database
Validation error is part of the wtforms - import it - go up
"""
def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


#create login form
class LoginForm(FlaskForm):
    #can login either with username or email: can remove this one: username = StringField('username', validators=[DataRequired(),Length(min=2, max=20)])
    email=StringField('email', validators=[DataRequired(),Email()])
    password = PasswordField('password', validators=[DataRequired()])
    #to stay login use secure cookie
    remember=BooleanField('Remember Me')
    submit=SubmitField('login')


