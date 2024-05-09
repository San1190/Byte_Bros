def suma():
    n1 = int(input("Numero 1: "))
    
    n2 = int(input("Numero 2: "))
    print(n1 + n2)
    print("Gracias por sumar")





try:
    suma()

except TypeError:
    print("Estás intentando concatenar tipos distintos")

except ValueError:
    print("El caracter introducido no es un número")
else:
    print("Hiciste todo bien")


finally:
    print("Eso fue todo.")
