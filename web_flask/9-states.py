#!/usr/bin/python3
"""Starts a Flask wa, server must listen 0.0.0.0 port 5000.
   route (/states and /states/<id>)"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def tear_all(self):
    storage.close()

@app.route("/states", strict_slashes = False, defaults={'id':0})
@app.route("/states/<id>", strict_slashes = False)
def state_city_list(id):
    states = storage.all("State")
    class_name = "States"
    return render_template("9-states.html", states=states, class_name=class_name, stateid=id)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
