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


@app.route("/data")
@app.route("/data/<int:ndata>")
def data(ndata=100):
    """
    On request, this returns a list of ``ndata`` randomly made data points.

    :param ndata: (optional)
        The number of data points to return.

    :returns data:
        A JSON string of ``ndata`` data points.

    """
    x = 10 * np.random.rand(ndata) - 5
    y = 0.5 * x + 0.5 * np.random.randn(ndata)
    A = 10. ** np.random.rand(ndata)
    c = np.random.rand(ndata)
    return json.dumps([{"_id": i, "x": x[i], "y": y[i], "area": A[i],
        "color": c[i]}
        for i in range(ndata)])

@app.route("/gdata")
@app.route("/gdata/<float:mux>/<float:muy>")
def gdata(ndata=100,mux=.5,muy=0.5):
    """
    On request, this returns a list of ``ndata`` randomly made data points.
    about the mean mux,muy

    :param ndata: (optional)
        The number of data points to return.

    :returns data:
        A JSON string of ``ndata`` data points.

    """

    """Instead of getting values from URL, try from request object"""
    mux = request.args.get('mux', '')
    muy = request.args.get('muy', '')

    x = np.random.normal(mux,.5,ndata)
    y = np.random.normal(muy,.5,ndata)
    A = 10. ** np.random.rand(ndata)
    c = np.random.rand(ndata)
    return json.dumps([{"_id": i, "x": x[i], "y": y[i], "area": A[i],
        "color": c[i]}
        for i in range(ndata)])

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