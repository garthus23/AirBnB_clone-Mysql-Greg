#!/usr/bin/python3

from flask import Flask, render_template

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

@app.route('/number/<int:n>', strict_slashes=False)
def isnumber(n):
    return "%d is number" % n

@app.route('/number_template/<int:n>', strict_slashes=False)
def dispnpage(n):
    return render_template("5-number.html", value=n)

if __name__ == "__main__":
    app.run()
