#!/usr/bin/python3
"""Module that starts a Flask web application"""
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def list_state():
    #Displays a list of cities in their states in a website
    state_list = storage.all(State).values()
    return render_template('8-cities_by_states.html', state_list=state_list)


@app.teardown_appcontext
def close_storage(db):
    #Closes the current SQLAlchemy session
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
"""
#!/usr/bin/python3
"""
Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states')
def display_states_cities():
    """Display the states and cities sorted by state and city name"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)