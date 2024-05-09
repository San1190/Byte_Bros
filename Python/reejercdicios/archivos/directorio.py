import os

ruta = 'C:\\Users\\sanfu\\Desktop\\p6ython\\reejercdicios\\archivos\\prueba.txt'

elemento = os.path.basename(ruta)
elemento2 = os.path.dirname(ruta)
print(elemento)
print(elemento2)

elemento3 = os.path.split(ruta)
print(elemento3)    

