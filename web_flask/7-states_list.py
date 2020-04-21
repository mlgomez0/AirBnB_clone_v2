#!/usr/bin/python3
"""Starts a Flask wa, server must listen 0.0.0.0 port 5000.
   route (/states_list)"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def tear_all(self):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def state_list():
    st = storage.all("State")
    cn = "States"
    return render_template("7-states_list.html", states=st, class_name=cn)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
