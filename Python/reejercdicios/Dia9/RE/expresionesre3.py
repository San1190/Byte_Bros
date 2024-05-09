import re

clave = input("Clave: ")

patron = r'\D{1}\w{7}'

c = re.search(patron,clave)

print(c.group())
