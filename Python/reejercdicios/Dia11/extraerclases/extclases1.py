import bs4
import requests

pag = requests.get("https://escueladirecta.com/blog/260007/encapsulamiento")

sopa = bs4.BeautifulSoup(pag.text, 'lxml')




columna = sopa.select('.course-listing-title')

for p in columna:
    print(p.getText())
#print(columna)
