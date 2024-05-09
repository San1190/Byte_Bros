import os


ruta = os.chdir("C:\\Users\\sanfu\Desktop\\alternativa") #cambiar directorio


archivo = open('otro_archivo.txt')
print(archivo.read())
#print(ruta)


ruta2 = os.makedirs("C:\\Users\\sanfu\Desktop\\alternativa\\otra")#crear carpetas

