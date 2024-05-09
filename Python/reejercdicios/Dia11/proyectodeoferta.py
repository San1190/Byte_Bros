import bs4
import requests


#crear pagina sin numero
url_base = "https://www.pccomponentes.com/ofertas-especiales?page={}"

#lista de nombres de oferta
nombre_con_oferta = []

#lista de precios
precios_oferta = []

#iterar objetos
for pagina in range(1,10):
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado, "lxml")
    
