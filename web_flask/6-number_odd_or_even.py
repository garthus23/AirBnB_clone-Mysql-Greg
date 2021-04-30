#!/usr/bin/python3


""" module tout mou """
from flask import Flask, render_template


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
    return 'Python %s' % text


@app.route('/number/<int:n>', strict_slashes=False)
def isnumber(n):
    """ is number """
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def dispnpage(n):
    """ dispnpage """
    return render_template("5-number.html", value=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oddoreven(n):
    """ is even or odd """
    if n % 2 == 0:
        value = 'even'
    else:
        value = 'odd'
    return render_template("6-number_odd_or_even.html", value=value, number=n)


if __name__ == "__main__":
    app.run()
