from functions import *
from newsfunctions import *
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('search.html')

@app.route('/results', methods = ['GET', 'POST'])
def results():
    # if request.method == 'POST':
    search = request.form['search_topic']
    domain = request.form['domain']
    news_articles = extract_news(search, domain)
    return render_template('newscatcher.html', news_articles=news_articles)

