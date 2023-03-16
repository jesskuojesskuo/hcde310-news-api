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
    search = request.form['search_topic']
    domain = request.form['domain']
    nyt_articles = get_articles(search)
    news_articles = extract_news(search, domain)
    return render_template('nyt.html', nyt_articles=nyt_articles)
    # return render_template('newscatcher.html', news_articles=news_articles)