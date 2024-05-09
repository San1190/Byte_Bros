import bs4
import requests

url_base = "http://books.toscrape.com/catalogue/page-{}.html"
#web = requests.get(url_base)

resultado = requests.get(url_base.format('1'))

sopa = bs4.BeautifulSoup(resultado.text, "lxml")

libros = sopa.select(".product_pod")#se puede usar len para medir lo que vale la pag

estrellas = libros[0].select(".star-rating.Three") 

titulos = libros[0].select("a")[1]["title"]


#print(ejemplo)

print(titulos)


#for n in range(1,11):
#    print(url_base.format(n))