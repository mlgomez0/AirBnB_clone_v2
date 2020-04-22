#!/usr/bin/python3
"""Starts a Flask wa, server must listen 0.0.0.0 port 5000.
   route (/hbnb_filters)"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def tear_all(self):
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def state_city_list():
    return render_template("10-hbnb_filters.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
