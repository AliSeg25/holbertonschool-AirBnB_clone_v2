#!/usr/bin/python3
"""Flask web application"""
from flask import Flask, render_template
import sys
sys.path.append('/home/ali/holbertonschool-AirBnB_clone_v2')
from models import storage
from models.state import State
app = Flask(__name__)



@app.route('/states_list')
def states_list():
    states = storage.all("State")
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def close_storage(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)