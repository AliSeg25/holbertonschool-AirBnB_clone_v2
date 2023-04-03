#!/usr/bin/python3
""" Module to start a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def print_hello_hbnb():
    """ return sur la page "Hello HBNB!" """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)