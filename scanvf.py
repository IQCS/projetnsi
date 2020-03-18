import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os



CompteurParcours = 0

url = "scan-vf.net/solo-leveling/chapitre-1"

def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens = RecupListeLiens(soup)
    return [soup, ListeLiens]

def RecupListeLiens(soup):
    ListeLiens=[]
    img = soup.findAll('img')
    for item in img:
        if 'class' in item.attrs and item['class']==['img-responsive']:
            var = item['data-src']
            ListeLiens.append(var)
    return ListeLiens



def Next(soup):
    trunk = "scan-vf.net/solo-leveling/chapitre-"
    a = url.split('-')[-1]
    b = int(a)
    c= (b+1)
    d= str(c)
    NextUrl =trunk+d
    return NextUrl



