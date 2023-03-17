from functions import *
from newsfunctions import *
from flask import Flask, render_template, request, render_template_string
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('search.html')

@app.route('/results', methods = ['GET', 'POST'])
def results():
   if request.method == 'POST':
       search = request.form['search_topic']
       domain = request.form['domain']
       nyt_articles = get_articles(search)
       topic = nyt_articles['section'].split()[0].lower()
       news_articles = extract_news(topic, domain)

       nyt_template = render_template('nyt.html', nyt_articles=nyt_articles, search=search)
       newscatcher_template = render_template('newscatcher.html', news_articles=news_articles, domain=domain.upper(), topic=topic)

       search_template = render_template('search.html', search_topic=search, domain=domain)

       combined_template = search_template + nyt_template + newscatcher_template

       return render_template_string(combined_template)
   else:


       return 'Wrong HTTP method', 400
