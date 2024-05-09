lista = [1,"Dos",3]

buscar = 1 

#buscar in lista

#print(lista.index(buscar)) #saber la posicion (antes comprobar)


'''
if buscar in lista:
    print(lista.index(buscar))
else:
    print("No está en la lista")

'''
lista.append("Nuevo elemento") #añade un elemento al final

print(lista)

print(lista.count(3))#cuantas veces se encuentra

lista.insert(1,"hola")

print(lista)

i = (1,2,3,4)#tanto para "" o []
lista.extend(i)

print(lista)

lista.pop(2)

print(lista)

lista.remove("Nuevo elemento")

print(lista)

lista.reverse()

print(lista)