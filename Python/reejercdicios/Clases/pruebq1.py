from pathlib import Path
import re

lugar_cliente = Path('C:/Users/sanfu/Desktop/p6ython/reejercdicios/Clases/Clientes')


nom = input("Introduzca su nombre: ")
ape = input("Introduzca su apellido: ")
cuenta = str(len(nom))  +  str(len(ape)) + str(nom[0].upper())
  
cuenta1 = cuenta + '.txt'
archivo = open(lugar_cliente / cuenta1)
nums = []
for l in archivo:

    
 

    new_crazy = filter(str.isdigit, l)
    print(''.join(list(new_crazy)))


    
   
    
         
 
  

   