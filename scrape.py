import requests
from bs4 import BeautifulSoup
def scrape():
    url = "https://www.hindustantimes.com/rss/topnews/rssfeed.xml"
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'xml')

    news_data = []

    data = soup.findAll('item')

    for rows in data:
        collect = {}
        collect['title'] = rows.title.text
        collect['description'] = rows.description.text
        link = rows.link.text
        c = requests.get(link)
        next_soup = BeautifulSoup(c.content,'html5lib')
        collect['content'] = next_soup.findAll('p')
        news_data.append(collect)
    #print(news_data)
    return news_data

