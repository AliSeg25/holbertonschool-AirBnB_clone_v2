#!/usr/bin/python3
"""
Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
"""
from flask import Flask, render_template
import sys
sys.path.append('/home/ali/holbertonschool-AirBnB_clone_v2')
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Fetches data from storage engine"""
    data = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=data)


@app.teardown_appcontext
def close_session(response_or_exc):
    """Close the current SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
