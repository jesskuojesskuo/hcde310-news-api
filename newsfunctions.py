import urllib.parse
import urllib.request
import urllib.error
import json
import keys
import pprint
import requests

def extract_news(search,domain):
   url = "https://newsapi.org/v2/everything"


   querystring = {"q": search, "domains": domain,
                  "apiKey": keys.news_api_key,
                  "pageSize": 4}
   try:
       response = requests.request("GET", url, params=querystring)
       articles = response.json()['articles']
       parsed_articles = []
       for article in articles:
           article_info = {
               "title": article["title"],
               "description": article["description"],
               "source": article["source"]["name"],
               "content": article["content"],
               "author": article["author"],
               "date": article["publishedAt"],
               "link": article["url"],
       "imgurl": article["urlToImage"]
           }
           parsed_articles.append(article_info)
       return(parsed_articles)


   except urllib.error.URLError as e:
       print('The server couldn\'t fulfill the request.')
       print(f'Error code: {e.code}')

pprint.pprint(extract_news("finance", "cnn.com"))
