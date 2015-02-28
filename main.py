import flask
from flask import Flask
import pdb
import os

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DEBUG = True,
    SECRET_KEY = 'dev key',
    USERNAME = 'admin',
    PASSWORD = 'default'
))

from pages import *

if __name__ == "__main__":

    port = 8000

    # Open a web browser pointing at the app.
    os.system("open http://localhost:{0}/".format(port))

    # Set up the development server on port 8000.
    app.run(port=port)

