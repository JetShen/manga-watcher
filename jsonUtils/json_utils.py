import json
#utilities to json files 


def WriteF(manga):
    with open('jsonUtils/fav.json', 'w') as f:
        json.dump(manga, f)

def ReadF():
    with open('jsonUtils/fav.json', 'r') as f:
        fav = json.load(f)
    return fav


def WriteS(manga):
    with open('jsonUtils/selected.json', 'w') as f:
        json.dump(manga, f)

def ReadS():
    with open('jsonUtils/selected.json', 'r') as l:
        library = json.load(l)
    return library