import bs4
import requests

web = requests.get("https://www.escueladirecta.com/courses")

sopa = bs4.BeautifulSoup(web.text, "lxml")

imagenes = sopa.select(".course-box-image")[1]['src']

#print(imagenes)


imagen_curso_1 = requests.get(imagenes)

#print(imagen_curso_1.content)


f = open("ami_imagen.jpg", "wb")
f.write(imagen_curso_1.content)
f.close()

