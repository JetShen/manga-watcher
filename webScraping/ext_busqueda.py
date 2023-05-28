import requests
from bs4 import BeautifulSoup

def library(query):
    query = str(query)
    query = query.strip()
    query = query.replace(' ', '%20')
    page = requests.get("https://www.anime-planet.com/manga/all?name="+query)
    soup = BeautifulSoup(page.text ,'html.parser')
    lista = []
    i=1
    while(i<6):
        try:
            title= soup.select_one(f"#siteContainer > ul.cardDeck.cardGrid > li:nth-child({i}) > a > h3")
            link= soup.select_one(f"#siteContainer > ul.cardDeck.cardGrid > li:nth-child({i}) > a")
            manga={
                    "title": str(title.text),
                    "link": str("https://www.anime-planet.com")+str(link['href'])
                }
            lista.append(manga)
            i+=1
        except:
            if(i==1):
                error={
                    "title": "No se encontraron resultados",
                    "link": "https://www.anime-planet.com"
                }
                lista.append(error)
            break

    return lista

    
        

