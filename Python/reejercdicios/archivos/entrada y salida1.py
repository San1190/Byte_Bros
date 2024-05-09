mi_archivo = open('prueba.txt')
#son str
#print(mi_archivo)

#una_linea = mi_archivo.readline()
#print(una_linea.rstrip())
#
#una_linea = mi_archivo.readline()
#print(una_linea.upper())
#
#
#una_linea = mi_archivo.readline()
#print(una_linea.rstrip())
#
#print(mi_archivo.readline())
#print(mi_archivo.readline())
#print(mi_archivo.readline())


#print(mi_archivo.read())

#for l in mi_archivo:
#    print("Aqui dice: "+ l)








todas = mi_archivo.readlines()

todas = todas.pop()


print(todas)
mi_archivo.close()