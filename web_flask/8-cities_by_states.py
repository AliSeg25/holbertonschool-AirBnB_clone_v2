#!/usr/bin/python3
"""
Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
"""
from flask import Flask, render_template
import sys
from models import storage
from models.state import State


sys.path.append('/home/ali/holbertonschool-AirBnB_clone_v2')
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=sorted_states)


@app.teardown_appcontext
def storage_close(db):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
