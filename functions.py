import urllib.parse, urllib.request, urllib.error, json
import requests
import pprint
import keys
import random

url = "https://api.newscatcherapi.com/v2/search"

querystring = {"q":"\"Elon Musk\"","lang":"en","sort_by":"relevancy","page":"1"}

headers = {
    "x-api-key": "PTEwAAdNgTVBTSJytLZu6yE1HknzVECA0QdaYxHr7zs"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


# AUSTIN
# https://api.nytimes.com/svc/archive/v1/2019/1.json?api-key=XPTk3UQUOVyofZ6kfLYVtfn6pTv7HOTX

import urllib.parse, urllib.request, urllib.error, json
# import requests
import pprint
import keys
import random
from flask import Flask


def get_articles(year = 2000, month = 1):
    base_url = 'https://api.nytimes.com/svc/archive/v1/'
    url = (base_url + str(year) + "/" + str(month) + ".json?api-key=" + keys.api_key)

    print(url)

    try:
        x = urllib.request.urlopen(url)
        print("Success!!")
        return(json.loads(x.read()))
    except urllib.error.URLError as e:
        print('The server couldn\'t fulfill the request.')
        print(f'Error code: {e.code}')


# response = requests.get(api)
# data = response.json()


data = get_articles(1999, 1)
articles = data["response"]["docs"]

for article in data["response"]["docs"]:
    # print(article["headline"])
    print("SUMMARY 😎: " + article["abstract"])
    # print(article["web_url"])
    print("URL 🔗: " + article["web_url"] + "\n")

# print(data["docs"]["web_url"])

# selected = random.choice(articles)
# print(selected["headline"]["main"])
# print(selected["web_url"]["main"])
# print(articles)


# articles = get_articles(1999, 1)


# # for each of the articles in the list, get the information that is stored in a nested dictionary:
# headline = map(lambda x: x["headline"]["main"], articles)
# print("HEADLINE 🥰: " +str(headline))
# author = map(lambda x: x["headline"]["kicker"], articles)
# leadparagraph = map(lambda x: x["lead_paragraph"], articles)
# pubdate = map(lambda x: x["pub_date"], articles)

# # since keywords are a branch down in the nested dictionary, we need to add an additional for loop to collect all keywords:
# keywords = map(lambda x:list(i["value"] for i in x["keywords"]), articles)


# import pandas as pd
# data={'headline': list(headline), 'author': list(author), 'leadparagraph':list(leadparagraph),
#      'publication date': list(pubdate), "keywords": list(keywords)}
# df = pd.DataFrame(data)

# # exporting the data to csv:
# df.to_csv('NYT_data.csv')

# def get_emails(domain = "uw.edu"):

#     base_url = "https://api.hunter.io/v2/domain-search?domain="
#     url = (base_url + domain + "&api_key=" + keys.api_key)

#     try:
#         x = urllib.request.urlopen(url)
#         return(json.loads(x.read()))
#     except urllib.error.URLError as e:
#         print('The server couldn\'t fulfill the request.')
#         print(f'Error code: {e.code}')
