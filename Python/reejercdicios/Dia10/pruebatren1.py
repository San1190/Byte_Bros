import pygame 
import random
import math
from pygame import mixer

# Iniciar a pygame
pygame.init()

#Crear la pantalla
pantalla = pygame.display.set_mode((800,600))

#Titulo e icono:
pygame.display.set_caption("El juego de adivinar un número")


#Numeros
numeros_introducido = []
numero1 = []
numero2 = 0
numero3 = 0

#Juego:

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
    



#Ejecutar el juego
contador = 0
se_ejecuta = True
while se_ejecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        

        #Introducir números
        while contador < 3:

            if evento.type == pygame.KEYDOWN:
                 # Check for backspace
                if evento.type.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                    numero1 = numero1[:-1]
  
            # Unicode standard is used for string
            # formation
                else:
                    numero1 += evento.type.unicode
      


                if evento.type == pygame.K_0:
                    numero1.append(0)
                    

                elif evento.type == pygame.K_1:
                    numero1.append(1)

                elif evento.type == pygame.K_2:
                    numero1.append(2)

                elif evento.type == pygame.K_3:
                    numero1.append(3)

                elif evento.type == pygame.K_4:
                    numero1.append(4)

                elif evento.type == pygame.K_5:
                    numero1.append(5)

                elif evento.type == pygame.K_6:
                    numero1.append(6)

                elif evento.type == pygame.K_7:
                    numero1.append(7)

                elif evento.type == pygame.K_8:
                    numero1.append(8)

                elif evento.type == pygame.K_9:
                    numero1.append(9)

                if evento.type == pygame.K_RETURN:
                    break

            contador += 1

            

            
            





