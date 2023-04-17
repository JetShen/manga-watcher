import requests
from bs4 import BeautifulSoup

def Manga(link):
    page = requests.get(str(link))
    soup = BeautifulSoup(page.text ,'html.parser')
    title = soup.select_one('#main_content > div:nth-child(2) > div.row.no-gutters > div.col-12.p-2 > span.releasestitle.tabletitle').text
    img =soup.select_one('#main_content > div:nth-child(2) > div.row.no-gutters > div:nth-child(4) > div:nth-child(2) > center > img')['src']
    lastChapther = soup.select_one('#main_content > div:nth-child(2) > div.row.no-gutters > div:nth-child(3) > div:nth-child(17) > i:nth-child(1)').text
    genres = []
    for i in range(1, 5):
        g = soup.select_one('#main_content > div:nth-child(2) > div.row.no-gutters > div:nth-child(4) > div:nth-child(5) > a:nth-child('+str(i)+') > u').text
        genres.append(str(g))

    manga = {
        'title': str(title),
        'url': str(link),
        'img': str(img),
        'Chapthers': str(lastChapther),
        'genres': genres
    }

    return manga


