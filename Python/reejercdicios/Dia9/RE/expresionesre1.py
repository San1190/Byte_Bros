from cgitb import text
import re

texto = "Si necesitas ayuda llamada al (697)-456-5677 las 24 horas al servicio de ayuda"

patron = 'ayuda'
#palabra = 'ayuda' in texto
#print(palabra)

busqueda = re.findall(patron, texto) #search )= ehncuantra 1, findall encuentra todas -- hace una lista
print(busqueda)

#print(busqueda.span())
#print(busqueda.start())
#print(busqueda.end())

for h in re.finditer(patron,texto):
    print(h.span())