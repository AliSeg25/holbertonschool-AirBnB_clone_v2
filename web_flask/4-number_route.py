#!/usr/bin/python3
""" Module to start a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def print_hello_hbnb():
    """ return sur la page "Hello HBNB!" """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def print_hbnb():
    """ return sur la page "HBNB" """
    return "HBNB"


@app.route('/c/<text>')
def printctext(text):
    """ return c url"""
    return "c {}".format(text.replace('_', ' ')).capitalize()


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def printpython(text):
    """ return python url"""
    return "python {}".format(text.replace('_', ' ')).capitalize()


@app.route('/number/<int:n>', strict_slashes=False)
def print_n(n):
    """print n """
    return "{} is a un number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
