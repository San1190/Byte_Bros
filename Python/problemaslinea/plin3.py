from math import sin, cos, tan, exp, log

def funcion(f, n):
    functions = {'sin':sin, 'cos':cos, 'tan':tan, 'exp':exp, 'log':log}
    result = {}
    for i in range(1, n+1):
        result[i] = functions[f](i)
    return result

def Calculator():

    f = input("Introduce la función: ")
    n = int(input("Introduce un número entero positivo: "))

    for i, j in funcion(f,n).items():
        print(i, '\t', j)

    return

Calculator()






    
