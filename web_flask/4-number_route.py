#!/usr/bin/python3
"""Starts a Flask wa, server must listen 0.0.0.0 port 5000.
    aditional route (/number/<n>)"""

from flask import Flask
app = Flask(__name__)
@app.route("/", strict_slashes = False)
def home():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes = False)
def hbpage():
    return "HBNB"

@app.route("/c/<text>", strict_slashes = False)
def varpage(text):
    str_show = str(text).replace("_", " ")
    return "C " + str_show

@app.route("/python", strict_slashes = False, defaults={'text':"is cool"})
@app.route("/python/<text>", strict_slashes = False)
def varpagepy(text):
    str_show = str(text).replace("_", " ")
    return "Python " + str_show

@app.route("/number/<int:n>", strict_slashes = False)
def varpagenum(n):
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
