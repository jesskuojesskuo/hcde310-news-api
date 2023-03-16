import urllib.parse, urllib.request, urllib.error, json
import keys

def get_articles(input):
    base_url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q='
    output_string = input.replace(" ", "-")
    url = (base_url + str(output_string) + "&api-key=" + keys.api_key)

    try:
        x = urllib.request.urlopen(url)
        print("Success!!")
        data = json.loads(x.read())

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
                "author": article["byline"]["original"],
                "date": article["pub_date"],
                "link": article["web_url"],
                "imgurl": first_image_url
                }
            return article_info

    except urllib.error.URLError as e:
        print('The server couldn\'t fulfill the request.')
        print(f'Error code: {e.code}')