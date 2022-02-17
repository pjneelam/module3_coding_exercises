"""
step1ii)
for the app to work, import app from __init__.py file
"""

from flaskblog import app



"""
Line below: to run the application.
The debug parameter is set to true. Makes it possible to re-initialise the homepage without re-starting the server.
to synchonise your updates in the codes and the web page, RUN the program and check if Debug mode is on in the Terminal below
to turn it on, run code: set FLASK_DEBUG=1
To note: in a production environment, it must be set to False to avoid any security issues.
"""

if __name__ == '__main__':
    app.run(debug=True)


"""
page created: http://127.0.0.1:5000/


to style your web page (homepage.html), use styling framework "Bootstrap" - https://getbootstrap.com/docs/4.5/getting-started/introduction/#starter-template

create HEROKU account. Different database: sqllite for testing/development and postgresql for production/deployment

step 2: create the wtforms.py
pip3 install flask-wtf
"""

