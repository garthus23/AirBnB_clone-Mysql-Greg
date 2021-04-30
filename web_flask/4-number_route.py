#!/usr/bin/python3


""" module flask tout mou """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index0():
    """ index 0 """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def index1():
    """ index 1 """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cvalue(text):
    """ cvalue """
    text = text.replace('_', ' ')
    return "C %s" % text


@app.route('/python', strict_slashes=False)
def pyvalue():
    """ pyvalue """
    return "Python is cool"


@app.route('/python/<text>', strict_slashes=False)
def pytxtvalue(text):
    """ pytxtvalue """
    text = text.replace('_', ' ')
    return 'Python is %s' % text

@app.route('/number/<int:n>', strict_slashes=False)
def isnumber(n):
    """ isnumber """ 
    return "%d is number" % n


if __name__ == "__main__":
    app.run()
