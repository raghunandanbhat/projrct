import requests
from bs4 import BeautifulSoup


def getDataFromWiki(cat):
    url = "https://en.wikipedia.org/wiki/" + cat
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'xml')

    news_data = []

    data = soup.findAll('p')

    for row in data:
        news_data.append(row.text)
    return "".join(news_data)


print (getDataFromWiki('google'))