#!/usr/bin/python3
"""Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def récuperer_donnée():
    # Utiliser le storage pour récuperer les données
    state_list = storage.all(State).values()
    print(state_list)
    return render_template('8-cities_by_states.html', state_list=state_list)


@app.teardown_appcontext
def storage_close(db):
    # fermer la session
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
