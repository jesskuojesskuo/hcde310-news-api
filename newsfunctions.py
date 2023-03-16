import urllib.parse
import urllib.request
import urllib.error
import json
import keys
import pprint


def extract_news_url(search,domain):
    base_url = "https://newsapi.org/v2/everything"
    url = (base_url + "?q=" + search + "&domain=" + domain + "&apiKey=" + keys.news_api_key)

    try:
        x = urllib.request.urlopen(url)
        articles = json.loads(x.read())['articles']
        parsed_articles = []
        for article in articles:
            article_info = {
                "title": article["title"],
                "description": article["description"],
                "source": article["source"]["name"],
                "content": article["content"],
                "author": article["author"],
                "date": article["publishedAt"],
                "link": article["url"]
            }
            parsed_articles.append(article_info)
        return(parsed_articles)

    except urllib.error.URLError as e:
        print('The server couldn\'t fulfill the request.')
        print(f'Error code: {e.code}')

pprint.pprint(extract_news_url("finance"))