import random
from random import randint
# juego de los 8 intentos

n = input("¿Cúal es tu nómbre? ")
print(f"Bienvenid@ {n}, vas a jugar al juego de adivinar un número del 1 al 100\n")
r = random.randint(1,100)

cont = 0
while cont < 8:

    num = int(input("Coloque un número del 1 al 100: "))

    if num not in range(1,101):
        print("El número escogido esta fuera del rango permitido")
    elif num < r:
        print("El número buscado es mayor")
    elif num > r:
        print("El número buscado es menor")
    else:
        print(f"Enhorabuena!!, Has acertado el número en {cont} intentos. :)")
        break

    cont+=1

if cont == 8:
    print(f"Lo siento, el número seleccionado era el {r}")
    
