#numero con distintocs codigos 3 areas : perfumeria, farmacio cosmetica : a cua lse dirigfe y u'n numero  C-54 ;  (otro turno)
from numerosproyecto8 import *
from os import system
def Menu():

    system('cls')
    print('''Bienvenid@ a la tienda. Por favor seleccione donde desea comprar:
    |1| - Farmacia
    |2| - Cosmeticos
    |3| - Perfumeria
    |4| - Salir
    
    -Se le asignará un número en base a lo escogido. Gracias por todo. -''')



def Mensajes(n):
    if n == 1:
        x = input("\n-Presione 'enter' para voler al inicio-")



def preguntar():
    
    while True:

        Menu()       
    
        try:
            nums = [1, 2, 3, 4]
            n = int(input("-"))

            nums.index(n)

        except ValueError:
                print("ERROR, COLOQUE SOLAMENTE EL NÚMERO")

                Mensajes(1)

        else:
            break
    Decorar(n)






def seguir():
    while True:
        preguntar()
        try:
            turno = input("Quieres sacar otro número? |S| |N|: ").upper()
            ['S', 'N'].index(turno)

        except ValueError:
            print("ERROR, LO INTRODUCIDO NO ES UNA OPCIÓN VALIDA")

            Mensajes(1)
            

        else:
            if turno == 'N':
                print("Gracias por la visita")
                break

            else:
                system('cls')






seguir()