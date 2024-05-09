from random import choice
from os import system
from tkinter import *
palos_jugador = []
numeros_jugador = []
palos_crupier = []
numeros_crupier = []
figuras =["J", "Q", "R"]
intentos = 2





## iniciar tkinter
#aplicacion = Tk()
#
##tamaño pantalla
#aplicacion.geometry('1160x550+0+0')
#
## evitar maximizar
#aplicacion.resizable(0, 0)
#
## titulo de la ventana
#aplicacion.title("Black")
#
## color de fondo de la ventana
#aplicacion.config(bg='burlywood')





def Carta():
    numeros = [1,2,3,4,5,6,7,8,9, 11, 10 , 10 , 10 , 12]
    palos = ['♥','♠','♣', '♦']
    
    
    palo_seleccionado = choice(palos)

    numero_seleccionado = choice(numeros)

 



    return palo_seleccionado , numero_seleccionado




def Crupier(tiradas):
    palos = []
    numeros = []
    figuras =["J", "Q", "R"]
    As = ["A"]
    contador = 0
    while contador < tiradas:
        palo , numero = Carta()


        if numero == 12:
             numero = 11

        

        palos.append(palo)
        numeros.append(numero)
        contador += 1
    
 

    
    return numeros



def Jugador(intentos):

    palos = []
    numeros = []
    
    As = ["A"]
    contador = 0
    while contador < 2:
        palo , numero = Carta()


        if numero == 10:
            numero = choice(figuras)

        elif numero == 11:
            numero = 10
        
        elif numero == 12:
            numero = As[0]

        palos.append(palo)
        numeros.append(numero)
        contador+= 1


    carta1 = str(numeros[0]) +  palos[0]
    carta2 = str(numeros[1]) +  palos[1]
    print(f"La primera carta es: {carta1}")
    print(f"La segunda carta es: {carta2}")


    if numeros[0] == 'J' or 'Q' or 'R' :
        numeros[0] = 10

    if numeros[1] == 'J' or 'Q' or 'R' :
        numeros[1] = 10

    if numeros[0] == 'A':
        numeros[0] = 11

    if numeros[1] == 'A':
        numeros[1] = 11

    if numeros[0] + numeros[1] == 21:
        Ganar()

    for num in numeros:
        numeros_jugador.append(num)

    for pal in palos:
        palos_jugador.append(pal)

    otra_tirada(intentos)







def otra_tirada(intentos):
 
 
    contador2 = True
    num = 2
    suma = 0
    while contador2:
        intentos += 1
        
        pregunta = int(input('''QUÉ DESEA HACER?
            |1|- Pedir otra carta más.
            |2|-Plantarse.
            -Escriba el número: '''))
        if pregunta == 1:
            
            system('cls')
            print("Ha seleccionado otra carta.")
            palo_m , numero_m = Carta()
            palos_jugador.append(palo_m)
            numeros_jugador.append(numero_m)
            
            if numero_m  == 10:
                numero_m  = choice(figuras)
            elif numero_m  == 11:
                numero_m  = 10
    
            elif numero_m  == 12:
                numero_m  = 'As'

            cartax = str(numeros_jugador[num]) + palos_jugador[num]
            print(cartax)
            num += 1
            for n in numeros_jugador:
                suma += n
            if suma > 21:
                Perder_pasarse(suma)
                break
            





            
                 
        elif pregunta == 2:
            contador2 = False
            Comprobar()


        
            
                
                
                


def Comprobar():
    numeros_cru = 0
    numeros_ju = 0

    for num in numeros_jugador:
        numeros_ju += num
    
    
    numeros_crupier = Crupier(intentos)
    
    

    for num_cru  in numeros_crupier:
        numeros_cru += num_cru


    if numeros_ju > numeros_cru:
        system('cls')
        Ganar(numeros_ju, numeros_cru)
    
    else:
        system('cls')
        Perder(numeros_ju, numeros_cru)



    


    return 0

def Ganar(puntos_tuyos, puntos_crupier):
    
    print("*"*20)
    print("FELICIDADES, HA GANADO 😊")
    print(f"Suma total suya : {puntos_tuyos}")
    print(f"Suma del crupier total: {puntos_crupier}")
    print("*"*20)

   

def Perder(puntos_tuyos, puntos_crupier):
    
    print("*"*20)
    print("FELICIDADES, HA PERDIDO 😥")
    print(f"Suma total suya : {puntos_tuyos}")
    print(f"Suma del crupier total: {puntos_crupier}")
    print("*"*20)



def Perder_pasarse(puntos_tuyos):
    print("*"*20)
    print("FELICIDADES, HA PERDIDO POR PASARSE 😥")
    print(f"Suma total suya : {puntos_tuyos}")
    
    print("*"*20)






Jugador(intentos)



         
