x = float(input("Pon un número :"))
y = float (input("Pon otro número: "))
op = input("Escribe que operación desea efectuar:")

def sum(x, y):
    return x + y
def rest(x, y):
    return x - y
def mult(x,y):
    return x * y 
def div(x, y):
    return x / y
def res(x , y):
    return x % y
def pot(x,y):
    return x **y
#def cua(x,y):
#    return




if op == "suma":
    print(sum(x,y))
elif op == "resta":
    print("Tu respuesta es:")
    print(rest(x,y))
elif op == "multiplicación":
    print(mult(x,y))
elif op == "división":
    print(div(x,y))
elif op == "resto":
    print(res(x,y))
elif op == "potencia":
    print(pot(x,y))

