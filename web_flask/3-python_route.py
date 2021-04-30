#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index0():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def index1():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def cvalue(text):
    return "C %s" % text

@app.route('/python', strict_slashes=False)
def pyvalue():
    return "Python is cool"

@app.route('/python/<text>', strict_slashes=False)
def pytxtvalue(text):
    return 'Python is %s' % text

if __name__ == "__main__":
    app.run()
