

archivo = open("prueba.txt",'a')#a = al final, agregar , no escribir / w =escribir / r= leer

archivo.write("Soy el nuevo texto")# lo sobrescribe y no hace \ n
archivo.write("Hola")

archivo.write('''hola
mundo
como 
estoy''')

archivo.writelines(['hola','mundo','como'])#los escribe todos juntos

lista =['hola','mundo','como']
for p in lista:
    archivo.writelines(p + '\n')





archivo.close()