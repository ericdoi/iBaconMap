import json
import flask
from flask import render_template, session, redirect, url_for, escape, request, flash
from main import app
import numpy as np
#from utilFunctions import *
import os

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.static_folder, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

##### Page Routes ####

@app.route("/")
def mindex():
    """
    Get map template.
    """
    return flask.render_template("map.html")

@app.route("/getdists")
def getdists():
    """
    Simulates json data from server.
    """
    scale = 20
    testData = [
        {"user_id":"39CA2D06-DEC6-45A2-B8A0-90D0C4754EC0",
            "uuid":"E20A39F4-73F5-4BC4-A12F-17D1AD07A961",
            "proximity":str(5.0 + 3.0*np.random.normal())},
        {"user_id":"DAFKHASLKFJALSJFLSAKJFLSAKJFLASKJLKS",
            "uuid":"ASKJASLJDLKSAJLDKJASLKJDALSKDLSKAJDL",
            "proximity":str(10.0 + 3.0*np.random.normal())}
     ]
    return json.dumps(testData)

@app.route("/test")
def test():
    """
    Test: print out simple json.
    """
    x = 10 * np.random.rand(5)
    return flask.jsonify({'name':'Eric', 'Lname':'Doi'})