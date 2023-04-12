import requests
from bs4 import BeautifulSoup
#busqueda de maximo 5 titulos por momento
# #si la ruta no tiene el tag i buscar el nombre en el tag a

query = str(input("Introducir serie: "))
query = query.replace(' ', '+')
page = requests.get("https://www.mangaupdates.com/search.html?search="+query)
soup = BeautifulSoup(page.text ,'html.parser')

biblio_query = {}

lista = []

i=5
while(i<22):
    search_one = soup.select_one('#main_content > div > div:nth-child(5) > div:nth-child('+str(i)+') > a > i')
    if(search_one == None):
        search_one = soup.select_one('#main_content > div > div:nth-child(5) > div:nth-child('+str(i)+') > a')
    i+=4
    lista.append(search_one)

for i in lista:
    print(i)



# uno = soup.select_one('#main_content > div > div:nth-child(5) > div:nth-child(5) > a > i')
# dos = soup.select_one('#main_content > div > div:nth-child(5) > div:nth-child(9) > a > i')
# tres = soup.select_one('#main_content > div > div:nth-child(5) > div:nth-child(13) > a')


# enlace = dos['href']
# print("enlace: ", enlace)

# link = tres['href']
# print("link: ", link)