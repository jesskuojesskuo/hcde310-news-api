
from functions import *

from flask import Flask, render_template, request

# Create an instance of Flask

app = Flask(__name__)

# Create a view function for /
@app.route('/')
def index():
    search = "test"
    return render_template('search.html', results = search)

@app.route("/search")
def search():
    input = request.args.get("search")
    input_category = request.args.get("category")
    results = get_articles(input, input_category)
    return(results)