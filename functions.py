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
#
# import urllib.parse, urllib.request, urllib.error, json
# # import requests
# import pprint
# import keys
# import random
# from flask import Flask
#
#
# def get_articles(year = 2000, month = 1):
#     base_url = 'https://api.nytimes.com/svc/archive/v1/'
#     url = (base_url + str(year) + "/" + str(month) + ".json?api-key=" + keys.api_key)
#
#     print(url)
#
#     try:
#         x = urllib.request.urlopen(url)
#         print("Success!!")
#         return(json.loads(x.read()))
#     except urllib.error.URLError as e:
#         print('The server couldn\'t fulfill the request.')
#         print(f'Error code: {e.code}')
#
#
# # response = requests.get(api)
# # data = response.json()
#
#
# data = get_articles(1999, 1)
# articles = data["response"]["docs"]
#
# for article in data["response"]["docs"]:
#     # print(article["headline"])
#     print("SUMMARY 😎: " + article["abstract"])
#     # print(article["web_url"])
#     print("URL 🔗: " + article["web_url"] + "\n")