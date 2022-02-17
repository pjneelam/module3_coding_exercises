"""
step 2
returning HTML in Flask, create all html pages (e.g homepage.html in another folder called templates)
add render_template method (to connect to the html template)

url_for= is used for creating a URL to prevent the overhead of having to change URLs 
throughout an application (including in templates). 
Without url_for , if there is a change in the root URL of your app then you have to change it
in every page where the link is present.

flash= for flash messages (e.g message on registration etc.)

redirect=to redirect the user to the homepage, for instance, after having registered.

request=
"""


from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm

"""
import users and posts from models.py
circular error with db: import user,post after having db=SQLAlchemy(app)
"""
from flaskblog.models import User, Post

"""
see models.py file, which was created to restructure the application as a package rather than a module
so, instead of putting the classes (Post, User) here, a new file was created

login_required = a decorator: means user has to log in to see the other pages

A decorator is a design pattern in Python that allows a user to add new functionality
to an existing object without modifying its structure. 
Decorators are usually called before the definition of a function you want to decorate. [https://www.datacamp.com/community/tutorials/decorators-python]

"""

from flask_login import login_user, current_user, logout_user, login_required

#example posts
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]



#create a route (url) - that will lead to the webpage created.
@app.route('/')
#to go directly to the home page, add another route
#homepage.html and all other html files must be created in a folder called "templates"
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/Workspace')
def workspace():
    return render_template('workspace.html')

@app.route('/register',methods=['GET','POST'] )
def register():
    #when user is already logged in, can't re-login/re-register
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form=RegistrationForm()
    if form.validate_on_submit():
        #create the hashed password by using bcrypt and passing all the users' fields 
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        #'success'> bootstrap 
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for("login"))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            """
            ternary condition in Python: 
            Ternary operators are also known as conditional expressions are operators that evaluate something based on a condition being true or false.
            It simply allows testing a condition in a single line replacing the multiline if-else making the code compact.
            Source: https://www.geeksforgeeks.org/ternary-operator-in-python/
            """
            return redirect(next_page) if next_page else redirect(url_for('homepage'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('homepage'))

"""To put restrictions on certain routes, and you can go to the routes only if you are logged in"""
@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')



