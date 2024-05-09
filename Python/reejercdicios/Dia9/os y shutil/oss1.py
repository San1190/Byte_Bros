import os


import os

print(os.getcwd())

archivo = open("curso.txt", 'w')
archivo.write("texto de prueba")
archivo.close()
print(os.listdir())