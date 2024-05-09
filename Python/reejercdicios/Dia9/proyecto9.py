#import zipfile
#
#zip_abierto = zipfile.ZipFile("Proyecto+Dia+9.zip","r")
#
#zip_abierto.extractall()

import re
import os
import time
import datetime
from pathlib import Path
import math

inicio = time.time()
filtro = r"N\w{3}-\d{5}"
ruta = "C:\\Users\\sanfu\\Desktop\\Python\\reejercdicios\\Dia9\\Mi_Gran_Directorio"
archivos_encontrados = []
numeros_encontrados = []
hoy = datetime.date.today()



def filtrar(filtro, ruta):
    archivo = open(ruta,'r')
    texto = archivo.read()
    if re.search(filtro,texto):
        return re.search(filtro,texto)
    else:
        return None


def lista():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = filtrar(filtro, Path(carpeta , a))
            if resultado != None:
                numeros_encontrados.append(resultado.group())
                archivos_encontrados.append(a.title())



def iniciar():
    i = 0
    print("*" * 80)
    print(f"La fecha de busqueda es: {hoy.day}/{hoy.month}/{hoy.year} a las " + time.strftime("%X")+"\n")
    print("ARCHIVO\t\t\tNUM DE SERIE")
    print("-------\t\t\t------------")
    for a in archivos_encontrados:
        print(a +"\t\t" + numeros_encontrados[i])
        i+=1
    final = time.time()
    tiempo = final - inicio
    print(f"\nNúmeros encontrados: {i}")
    print(f"\nDuración de la búsqueda: {math.ceil(tiempo)}")
    print("*"*80)


lista()
iniciar()