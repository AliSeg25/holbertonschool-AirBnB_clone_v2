#!/usr/bin/python3
"""Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """Display a list of all State objects sorted by name"""
    state_list = storage.all(State).order_by(State.name)
    return render_template('7-states_list.html', state_list=state_list)


@app.teardown_appcontext
def close_storage(error):
    """Close the current SQLAlchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')