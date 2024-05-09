import bs4
import requests


resultado = requests.get("https://escueladirecta.com")

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

#print(sopa.select('title')[0].getText()) #busca lo que necesites

parrafo_especial = sopa.select('p')[3].getText()
print(parrafo_especial)