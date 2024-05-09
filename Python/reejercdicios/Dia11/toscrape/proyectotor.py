import bs4
import requests


#crear pagina sin numero
url_base = "http://books.toscrape.com/catalogue/page-{}.html"

#lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

#iterar paginas
for pagina in  range(1,51):

    #crear sopa en cda pag
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")

    #seleccionar libros de la pág
    libros = sopa.select(".product_pod")

    #iterar los libros
    for libro in libros:

        #comprobar las estrellas ( 4 0 5)
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:

            #guardar titulo en variable
            titulo_libro = libro.select("a")[1]["title"]

            #agregar libro a lista
            titulos_rating_alto.append(titulo_libro)


#ver los libros de 4 o 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)






