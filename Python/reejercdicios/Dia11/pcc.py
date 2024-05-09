import bs4
import requests


resultado = requests.get("https://www.pccomponentes.com/black-friday/portatiles")

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

#print(sopa.select('title')[0].getText()) #busca lo que necesites

#parrafo_especial = sopa.select('p')[3].getText()
#print(parrafo_especial)
#crear pagina sin numero
url_base = "https://www.pccomponentes.com/black-friday/portatiles?page={}"

#lista de nombres de oferta
nombre_con_oferta = []

#lista de precios
precios_oferta = []

#iterar objetos
for pagina in range(1, 7):
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado, "lxml")
