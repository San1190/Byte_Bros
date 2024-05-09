from socket import AF_ROSE
from tkinter import N


def func(funcio,lista):

    list = []

    for i in lista:
        list.append(funcio(i))

    return list

def cuadrado(n):
    
    return n*n

print(func(cuadrado,[1,2,3,4]))