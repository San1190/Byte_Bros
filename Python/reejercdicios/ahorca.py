import random
import re
from random import randint, choice




palabras = ["casa","solo","sofa","pila", "mexico", "colombia", "canada", "venezuela", "uruguay", "argentina",
                      "guatemala", "panama", "ecuador","ford", "audi", "nissan", "renault", "chevrolet", "mitsubishi", "cadillac", "suzuki"]
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juegoterm = False

def pala(palabra):
    pa = choice(palabra)

    return pa


       

        
def comprobar_letra(palabra,letra):

    if letra in palabra:
        return True
    
    else:
        return False



    
def eletra():
    letra = input("\nColoque una letra: ").lower()

    while letra.isdigit() or  len(letra) != 1:
            print("ERROR , COLOQUE SOLAMENTE UNA LETRA")
            letra = input("Coloque una letra: ")

    return letra


def tablero(pal_eleguida):

    list = []

    for l in pal_eleguida:
        if l in letras_correctas:
            list.append(l)

        else:
            list.append("-")

    print(" ".join(list))



def checklet(letra_eleguida,palabra_oculta,vidas,coincidendcias):

    fin = False

    if letra_eleguida in palabra_oculta:
        letras_correctas.append(letra_eleguida)
        coincidendcias += 1

    else:
        letras_incorrectas.append(letra_eleguida)
        vidas -= 1
    
    if vidas == 0:
        fin = perder()
    elif coincidendcias == x-1:
        fin = ganar(palabra_oculta)
    
    return vidas, fin, coincidendcias




def perder():
    print("Te has quedado sin vidas")
    print(f"La palabra oculta era {palab}")

    return True


def ganar(palabra_descubierta):
    tablero(palabra_descubierta)
    print("Has encontrado la palabra")

    return True


#def val_letra():









def inicio():
    print("Bienvenido al juego del ahorcado ^^ ")






palab = pala(palabras)
x = len(palab)

while not juegoterm:
    
    inicio()
    print("\n" + "*" * 20 + "\n" )
    tablero(palab)
    print("\n")
    print("Letras incorrectas: " + "-".join(letras_incorrectas))
    print(f"vidas: {intentos}")
    letra = eletra()

    intentos , terminado, aciertos = checklet(letra,palab,intentos,aciertos)

    juegoterm = terminado



