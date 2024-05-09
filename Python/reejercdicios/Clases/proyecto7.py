#class Persona nombrte apellido
#
#class cliente (opersona) == num cuenta y balance . uno para imprimir todo , depositaer ( cuando dinero ) - retirar(Sacar dunero) (c
#odigo para que eliga tantas operaciones hjastra que slafga)
#crear cliente y devuelva al cliente y la otra el inicio
import os
from os import system
from pathlib import Path
from os import remove



lugar_cliente = Path('C:/Users/sanfu/Desktop/Python/reejercdicios/Clases/Clientes')





def Mensajes(n):
    if n == 1:
        x = input("\n-Presione 'enter' para voler al inicio-")


class Persona:
    def __init__(self,  nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido



           
           

def registro( c):
    registro = []
    for txt in os.listdir(lugar_cliente):
        registro.append(txt.removesuffix('.txt'))
    
    cliente = c
    if cliente in registro:
        print("Ya tiene una cuenta registrada. Por favor inicie sesión")
    
    else:
        print("Gracias por colaborar con nuetro banco")
        nom_arch = c +  '.txt'
        archivo = open(lugar_cliente / nom_arch , 'w')
        print("Cuenta creada con éxito!")
        archivo.close()
        Mensajes(1)


def sesion(n, a, c):
    sesion = []
    for txt in os.listdir(lugar_cliente):
        sesion.append(txt)
    cliente =  c +'.txt'
    for cliente in sesion:
        archivo = open(lugar_cliente / cliente)
        print("USUARIO: " + n +' ' + a)
        print("NÚMERO DE CUENTA: " + c)
        print(archivo.read())
        archivo.close()





    
class Cliente(Persona):
   

    def __init__(self, nombre, apellido, cuenta,balance):
        super().__init__(nombre, apellido)
        self.cuenta = cuenta
        self.balance = balance
        cuenta1 = self.cuenta + '.txt'
        archivo = open(lugar_cliente / cuenta1)

        for l in archivo:
            new_crazy = filter(str.isdigit, l)
            self.balance = int(''.join(list(new_crazy)))


    def imprimir(self): 
        system('cls')
        print("USUARIO REGISTRADO: " + self.nombre + " " + self.apellido + "\nNÚMERO DE CUENTA: " + self.cuenta + "\nBALANCE DE LA CUENTA: " + str(self.balance) + '€')
        Mensajes(1)

    def depositar(self):
        system('cls')
        n = int(input("Seleccione cuanta cantidad desea depositar a la cuenta: "))

        cuenta = self.cuenta + '.txt'
        archivo = open(lugar_cliente / cuenta , 'a+')

        self.balance += n

        #   accion = str(len(archivo.readlines()))
        

        archivo.write(f"ACTION ADD. NEW BALANCE: {self.balance}" + '\n')
        system('cls')

        print("Cantidad ingresada correctamente.")

        Mensajes(1)
    
    def retirar(self):
        system('cls')
        cc = int(input("Seleccione cuanta canditad desea retirar de la cuanta:"))
        
        if cc > self.balance:
            system('cls')
            print("ERROR, NO PUEDE RETIRAR MÁS DINERO DEL QUE TIENE.")
            Mensajes(1)
        
        else:
            
            system('cls')
            self.balance -= cc
            cuenta = self.cuenta + '.txt'
            archivo = open(lugar_cliente / cuenta , 'a+')
            #accion = str(len(archivo.readlines()))
            archivo.write(f"REMOVE ACTION. NEW BALANCE: {self.balance}"+ '\n')
            print("Cantidad retirada correctamente.")
            Mensajes(1)




def crear_cliente():

    system('cls')
   
    #cuenta =input("Introduzca su número de cuenta: ")
    system('cls')
    

    Menu2()
    n = int(input("-"))

    nom = input("Introduzca su nombre: ")
    ape = input("Introduzca su apellido: ")
    cuenta = str(len(nom))  +  str(len(ape)) + str(nom[0].upper())
   
    if n ==  1:
       sesion(nom , ape, cuenta)

    if n == 2:
       registro(cuenta)



    

    return nom, ape, cuenta

def Menu():
    system('cls')
    print('''Bienvenid@, coloque un número referente a lo que desea hacer:
    |1| - Información de la cuenta
    |2| - Retirar dinero
    |3| - Ingresar dinero
    |4| - Finalizar las acciones''')


def Menu2():
    system('cls')
    print('''Bienvenid@ a su terminal, coloque un número referente a lo que desea hacer:
    |1| - Iniciar sesión
    |2| -Registrarse''')
    

# Python3 program to convert a list
# of integers into a single integer
def convert(list):
      
    # Converting integer list to string list
    # and joining the list using join()
    res = int("".join(map(str, list)))
      
    return res

def inicio():
    system('cls')
    nom , ape, cuenta = crear_cliente()
    balance = 0
   #cuenta1 = cuenta + '.txt'

   #   archivo = open(lugar_cliente / cuenta1)
   #
  

   #for l in archivo:

   #      new_crazy = filter(str.isdigit, l)
   #   balance = int(''.join(list(new_crazy)))


   
    
    

    system('cls')
    

    
    terminado = False

    while terminado != True:
        Menu()
        cliente = Cliente(nom,ape,cuenta,balance)
        num = int(input("-"))


        if num == 1:
            cliente.imprimir()
        if num == 2:
            cliente.retirar()
        if num == 3:
            cliente.depositar()
        if num == 4:
            terminado = True 




    

inicio()
