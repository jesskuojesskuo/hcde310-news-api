
from functions import *

from flask import Flask, render_template, request

# Create an instance of Flask

app = Flask(__name__)

# Create a view function for /
@app.route('/')
def index():
    return render_template('search.html')
