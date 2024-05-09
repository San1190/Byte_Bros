import os
from pathlib import Path
from os import remove
from os import system


num_recetas = 0
lugar_recetas = Path('/Users/sanfu/Desktop/Recetas')
os.chdir(lugar_recetas)
categorias = os.listdir('/Users/sanfu/Desktop/Recetas')
recetas = []
paths = []

def Contar_Recetas(num_recetas):
    for txt in lugar_recetas.glob("**/*.txt"):
        print(txt)
        num_recetas += 1
       
    return num_recetas



for txt in lugar_recetas.glob("**/*.txt"):
    recetas.append(txt.name) 
    paths.append(txt) 


def Mensajes(n):
    if n == 1:
        x = input("\n-Presione 'enter' para voler al inicio-")

    if n == 2:
        print("El elemento seleccionado ha sido eliminado con éxito.")
    
    if n == 3:
        print("El elemento seleccionado ha sido creado con éxito")

    if n == 4:
        print("ERROR, el archivo no existe")
    
#-------------------------------------------------------------------------------------

def Leer_Recetas():
    
    system('cls')
    categoria = input(f"Escoja la categoria que desea leer:\n{categorias}\n -")
    
    recetas = ["|Recetas|"]
    
    system("cls")
    if categoria.capitalize() in os.listdir(lugar_recetas):
        for txt in os.listdir(lugar_recetas/categoria):
            recetas.append(txt.removesuffix('.txt'))
        print(recetas) 


    receta = input("Elige la receta: ")
    receta2 = receta + '.txt'
    system('cls')
    if receta in recetas:
        archivo = open(lugar_recetas / categoria / receta2)
        print(archivo.read())
        archivo.close()
        Mensajes(1)
         
    
   


#-------------------------------------------------------------------------------------


def Crear_Receta():

    categoria = input(f"En cual categoria desea elaborar  su receta {categorias}: ")
    system("cls")
    nom = input("Escriba el nombre con el cual quiera su receta: ")
    system("cls")
    nom_arch = nom + '.txt'
    archivo = open(lugar_recetas / categoria /nom_arch, "w")
    res = input("Escriba el contenido de su receta: ")
    archivo.write(res)
    system("cls")
    Mensajes(3)
    archivo.close()
    Mensajes(1)

#-------------------------------------------------------------------------------------

def Crear_Categoria():
    system('cls')
    categoria =input("Escriba el nombre de la categoria que deseé crear: ")
    os.mkdir(categoria)
    system('cls')
    Mensajes(3)
    Mensajes(1)
    


#-------------------------------------------------------------------------------------

def Eliminar_Receta():
    system('cls')
    categoria = input(f"Escoja la categoria que desea eliminar:\n{categorias}\n -")

    recetas = ["|Recetas|"]
    system("cls")
    if categoria.capitalize() in os.listdir(lugar_recetas):
        for txt in os.listdir(lugar_recetas/categoria):
            recetas.append(txt.removesuffix('.txt'))
        print(recetas) 


    receta = input("Elige la receta para eliminarla: ")
    receta2 = receta + '.txt'
    if receta in recetas:
        archivo = Path(lugar_recetas / categoria / receta2)
        remove(archivo)

        Mensajes(2)
        Mensajes(1)
    
    else:
        Mensajes(4)
        Mensajes(1)
        

    


def Eliminar_Categoria():
    system('cls')
    categoria = input(f"Escoja la categoria que desea eliminar:\n{categorias}\n -")
    
    if categoria in categorias:

        os.remove(categoria)
        Mensajes(2)
        Mensajes(1)
    else:
        Mensajes(4)
        Mensajes(1)





    


def Menu():
        system('cls')
        print("Seleccione que desea hacer:")
        print("1-Leer receta")
        print("2-Crear receta")
        print("3-Crear categoria")
        print("4-Eliminar receta")
        print("5-Eliminar categoria")
        print("6-Finalizar categoria")
        #n = int(input("Escriba aquí:"))
         

    

def Escoger():

    terminado = False

    while terminado != True:

        Menu()
        num= int(input("Escriba aquí:"))


        if num == 1:
            Leer_Recetas()

        if num == 2:
            Crear_Receta()

        if num == 3:
            Crear_Categoria()

        if num == 4:
            Eliminar_Receta()
        if num == 5:
            Eliminar_Categoria()
        if num == 6:
            terminado = True



Escoger()


        
