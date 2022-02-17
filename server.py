from flask import Flask

app = Flask(__name__)

@app.route('/')
def digitpol():
    return "Welcome to Digitpol"

if __name__ == '__main__':
    app.run(debug=True)
