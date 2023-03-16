
from functions import *

from flask import Flask, render_template, request

# Create an instance of Flask

app = Flask(__name__)

# Create a view function for /
@app.route('/')
def index():
    search = "test"
    return render_template('search.html', results = search)
    # return render_template('search.html', results = search)

# @app.route("/search")
# def search():
#     input = request.args.get("search")
#     input_category = request.args.get("category")
#     results = get_articles(input, input_category)
#     return(results)


@app.route('/search', methods=['GET', 'POST'])
def search():
    input = request.args.get("search")
    input_category = request.args.get("category")
    results = get_articles(input, input_category)
    return render_template('nyt.html', input = input, results = results)

    # place = request.form['place']
    # max_results = int(request.form['max_results'])
    # radius = float(request.form['radius'])
    # sort = True if request.form.get('sort') == 'true' else False
    # results = wikipedia_locationsearch(place, max_results, radius, sort)
    # return render_template('nyt.html')


# @app.route("/search")
# def search():
#     input = request.args.get("search")
#     input_category = request.args.get("category")
#     results = get_articles(input, input_category)
#     return(results)