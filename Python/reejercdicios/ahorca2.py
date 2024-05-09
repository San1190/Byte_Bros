import random
import time
 
## Listas de Palabras
marcas_de_coches = ["ford", "audi", "nissan", "renault", "chevrolet", "mitsubishi", "cadillac", "suzuki"]
 
nombres_de_paises = [ "mexico", "colombia", "canada", "venezuela", "uruguay", "argentina",
                      "guatemala", "panama", "ecuador"]
 
 
print("Bienvenido al juego de ahorcado")
time.sleep(2)
print("El objetivo del juego es adivinar la palabra secreta letra por letra")
print("tienes 5 vidas, pierdes una vida cada que te equivocas si te quedas sin vidas pierdes")
time.sleep(2)
 
print("Desea jugar con palabras de que son marcas de coches o nombres de paises")
time.sleep(2)
 
cat_seleccionada = input("Ingrese C para marcas de coches y P para nombres de paises: ")
 
while True:
    if cat_seleccionada.lower() == "c":
        print("excelente a seleccionado marcas de coches")
        palabra_secreta = random.choice(marcas_de_coches)
        break
    elif cat_seleccionada.lower() == "p":
        print("excelente a seleccionado nombres de paises")
        palabra_secreta = random.choice(nombres_de_paises)
        break
 
    else:
        print("Por favor seleccione una categoria valida")
        cat_seleccionada = input("Ingrese C para marcas de coches y P para nombres de paises: ")
 
 
 
## Es el numero de veces que se puede eqivocar
vidas = 5
 
lista_letras_adivinadas = []
 
## Imprimimos la palabra sin letras
print('_' * len(palabra_secreta))
 
while True:
 
    while True:
        letra_adivinada = input("Adivina una letra: ")
        if(len(letra_adivinada)!=1 and letra_adivinada.isnumeric()):
            print("Eso no es una letra intenta con una sola letra")
        else:
            if letra_adivinada.lower() in lista_letras_adivinadas:
                print("Ya habias intentado con esa letra intenta con otra por favor")
            else:
                lista_letras_adivinadas.append(letra_adivinada)
 
                if letra_adivinada.lower() in palabra_secreta:
                    print("Felicidades adivinaste una letra")
                    break
                else:
                    vidas = vidas-1
                    print("Te has equivocado y perdido una vida")
                    print("Te quedan " + str(vidas) + " vidas")
                    break
 
    if vidas==0:
        print("Haz perdido la palabra secreta era: "+ palabra_secreta)
        break
 
 
    estatus_actual = ""
 
    letras_faltantes = 0
    for letra in palabra_secreta:
 
 
        if letra in lista_letras_adivinadas:
            estatus_actual = estatus_actual + letra
 
        else:
            estatus_actual = estatus_actual + "_"
            letras_faltantes = letras_faltantes + 1
 
    ## Imprimir palabra con algunas letras
    print(estatus_actual)
 
 
    if letras_faltantes == 0:
        print("Felicidades haz ganado")
        print("La palabra secreta es: " + palabra_secreta)
        break