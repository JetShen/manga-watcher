import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.mangaupdates.com/series/6z1uqw7/solo-leveling")
soup = BeautifulSoup(page.text ,'html.parser')
titulo = soup.find('span', {'class': 'releasestitle tabletitle'}).text
print(titulo)