#!/usr/bin/python3
# flask app basic

""" module flask """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
""" define a return msg """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run()
