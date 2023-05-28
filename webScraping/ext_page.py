import requests
from bs4 import BeautifulSoup

def Manga(link):
    page = requests.get(str(link))
    soup = BeautifulSoup(page.text ,'html.parser')
    title = soup.select_one('#siteContainer > h1').text
    img =soup.select_one('#entry > div.pure-1.md-2-3 > div > div.pure-1-2.md-1-3 > div > img')['src']

    img_split = img.rsplit('/',1) 
    img_split = img_split[1]
    #extract and make a better name for the path
    img_split = img_split.split("t=")[1]
    img_split = f"{img_split}.png"

    lastChapters  = soup.select_one('#siteContainer > section.pure-g.entryBar > div:nth-child(1)').text
    parts = lastChapters.split("Ch:")
    #Get the second part after "Ch"
    lastChapters = parts[1]
    # Remove whitespace at the beginning and end of the string
    lastChapters = lastChapters.strip()
        

    Genders = []
    for i in range(1, 6):
        g = soup.select_one(f'#entry > div.pure-1.md-2-3 > div > div.pure-1.md-3-5 > div.tags > ul > li:nth-child({i}) > a').text
        g = g.strip()
        Genders.append(str(g))



    manga = {
        'title': str(title),
        'url': str(link),
        'img_link': str(img),
        'img_path':str(img_split),
        'Chapters': str(lastChapters ),
        'Genders': Genders
    }

    return manga


