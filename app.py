from functions import *
from newsfunctions import *
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('search.html')

@app.route('/results', methods = ['GET', 'POST'])

def results():
    if request.method == 'POST':
        domain = request.form['domain']
        query = request.form['search_topic']
        results = get_articles(query)
        return render_template('results.html', place=place, results=results)
    else:
        return 'Wrong HTTP method', 400