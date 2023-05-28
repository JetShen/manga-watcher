import requests
from bs4 import BeautifulSoup

def Manga(link):
    page = requests.get(str(link))
    soup = BeautifulSoup(page.text ,'html.parser')
    title = soup.select_one('#main_content > div:nth-child(2) > div.row.no-gutters > div.col-12.p-2 > span.releasestitle.tabletitle').text
    img =soup.select_one('#main_content > div:nth-child(2) > div.row.no-gutters > div:nth-child(4) > div:nth-child(2) > center > img')['src']

    img_split = img.rsplit('/',1) 

    lastChapters  = soup.select_one('#main_content > div:nth-child(2) > div.row.no-gutters > div:nth-child(3) > div:nth-child(17) > i:nth-child(1)')
    try:
        lastChapters  = lastChapters .text
    except:
        if ( lastChapters  == None):
            lastChapters  = soup.select_one('#main_content > div:nth-child(2) > div.row.no-gutters > div:nth-child(3) > div:nth-child(20)').text
            lastChapters .replace('\n', '')

    lastRelease =  soup.select_one('#main_content > div:nth-child(2) > div.row.no-gutters > div:nth-child(3) > div:nth-child(17) > i:nth-child(1)').text
    if (int(lastRelease)>int(lastChapters)):
        lastChapters = lastRelease
        

    Genders = []
    pop = False
    for i in range(1, 5):
        try:
            g = soup.select_one('#main_content > div:nth-child(2) > div.row.no-gutters > div:nth-child(4) > div:nth-child(5) > a:nth-child('+str(i)+') > u').text
            Genders.append(str(g))
        except:
            pop=True

    if(pop):
        Genders.pop()


    manga = {
        'title': str(title),
        'url': str(link),
        'img_link': str(img),
        'img_path':str(img_split[1]),
        'Chapters': str(lastChapters ),
        'Genders': Genders
    }

    return manga


