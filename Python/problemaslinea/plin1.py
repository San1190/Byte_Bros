 #Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, done n es el número introducido.

n = int(input("Seleccione un número del 1 al 10:"))

nombre = 'tabla-' + str(n) + '.txt'

f = open(nombre , 'w')

for i in range(1, 11):
    f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
f.close()