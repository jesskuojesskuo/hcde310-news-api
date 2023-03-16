import urllib.parse, urllib.request, urllib.error, json
import keys

# https://api.nytimes.com/svc/search/v2/articlesearch.json?q=election&api-key=
def get_articles(input):
    base_url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q='
    url = (base_url + str(input) + "&api-key=" + keys.api_key)

    try:
        x = urllib.request.urlopen(url)
        print("Success!!")
        data = json.loads(x.read())
        parsed_articles = []

        # Choose how many articles we want to print
        for article in data["response"]["docs"][0:1]:

            multimedia = article["multimedia"]
            first_image_url = None
            for media in multimedia:
                if media["type"] == "image":
                    first_image_url = "https://www.nytimes.com/" + media["url"]

            article_info = {
                "title": article["headline"]["main"],
                "description": article["abstract"],
                "section": article["section_name"],
                # "source": article["source"]["name"],
                # "content": article["content"],
                "author": article["byline"]["original"],
                "date": article["pub_date"],
                "link": article["web_url"],
                "imgurl": first_image_url
                }

            print(article_info)
            return article_info


            #
            # output_url = article["web_url"]
            # title = article["headline"]["main"]
            # abstract = article["abstract"]
            # date = article["pub_date"]
            # section = article["section_name"]
            #
            # multimedia = article["multimedia"]
            # first_image_url = None
            # for media in multimedia:
            #     if media["type"] == "image":
            #         first_image_url = "https://www.nytimes.com/" + media["url"]
            #
            # # add category (section_name), subsection name, and image url
            #
            # article_info = [output_url, title, abstract, date, section, first_image_url]
            # return (article_info)

            # return (article["web_url"])


            # return (article["web_url"], article["abstract"])

            # return("ARTICLE #" + str(article_count))
            # print("SUMMARY 😎: " + article["abstract"])
            # print("URL 🔗: " + article["web_url"] + "\n")


        # return(json.loads(x.read()))
    except urllib.error.URLError as e:
        print('The server couldn\'t fulfill the request.')
        print(f'Error code: {e.code}')
#


print(get_articles("hi"))
# def get_

# # response = requests.get(api)
# # data = response.json()
# #
# get_articles("washington", "business")


# def get_output(input):
#     get_articles("washington", "business")

# data = get_articles("university")
# # articles = data["response"]["docs"]
# #
# article_count = 1
# for article in data["response"]["docs"][0:5]:
#     # print(article["headline"])
#     print("ARTICLE #" + str(article_count))
#     article_count = article_count + 1
#     print("SUMMARY 😎: " + article["abstract"])
#     # print(article["web_url"])
#     print("URL 🔗: " + article["web_url"] + "\n")