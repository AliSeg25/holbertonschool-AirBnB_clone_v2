#!/usr/bin/python3
"""Flask web application"""
from flask import Flask, render_template
import sys
sys.path.append('/home/ali/holbertonschool-AirBnB_clone_v2')
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def récuperer_donnee():
    # Utiliser le storage pour récuperer les données
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def storage_close(db):
    # fermer la session
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
