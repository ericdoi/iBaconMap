import flask
from flask import Flask
import pdb
import os

app = Flask(__name__)

from pages import *

if __name__ == "__main__":

    port = 8000

    # Open a web browser pointing at the app.
    os.system("open http://localhost:{0}/".format(port))

    # Set up the development server on port 8000.
    app.debug = True
    app.run(port=port)

