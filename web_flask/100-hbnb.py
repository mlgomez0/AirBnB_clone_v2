#!/usr/bin/python3
"""Starts a Flask wa, server must listen 0.0.0.0 port 5000.
   route (/hbnb)"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def tear_all(self):
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def state_city_list():
    st = storage.all("State")
    am = storage.all("Amenity")
    pl = storage.all("Place")
    return render_template("100-hbnb.html", states=st, ameny = am, place = pl)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
