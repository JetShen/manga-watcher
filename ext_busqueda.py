import requests
from bs4 import BeautifulSoup
#busqueda de maximo 5 titulos por momento
# #si la ruta no tiene el tag i buscar el nombre en el tag a

def library(query):
    # query = str(input("Introducir serie: "))
    query = str(query)
    print("Estado de query: ", str(query))
    query = query.replace(' ', '+')
    page = requests.get("https://www.mangaupdates.com/search.html?search="+query)
    soup = BeautifulSoup(page.text ,'html.parser')
    lista = []
    j=5
    for i in range(0,5):
        search_one = soup.select_one('#main_content > div > div:nth-child(5) > div:nth-child('+str(j)+') > a')
        j+=4
        manga={
            "title": str(search_one.text),
            "link": str(search_one['href'])
        }
        lista.append(manga)

    for i in lista:
        print(i)

    return lista

