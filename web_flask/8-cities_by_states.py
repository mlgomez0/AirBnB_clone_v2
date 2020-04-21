#!/usr/bin/python3
"""Starts a Flask wa, server must listen 0.0.0.0 port 5000.
   route (/cities_by_states)"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def tear_all(self):
    storage.close()

@app.route("/cities_by_states", strict_slashes = False)
def city_list():
    states = storage.all("State")
    class_name = "States"
    return render_template("8-cities_by_states.html", states=states, class_name=class_name)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
