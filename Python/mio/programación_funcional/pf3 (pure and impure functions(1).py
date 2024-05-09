def pure_funcion(x, y):
    temp = x + 2*y
    return temp / (2*x + y)


some_list = []

def impure(arg):
    some_list.append(arg)

    """Las funciones puras son:
- más fáciles de razonar y probar.
- más eficiente. Una vez que se ha evaluado la función
 para una entrada, el resultado se puede almacenar y consultar la próxima vez que 
 se necesite la función de esa entrada, reduciendo el número de veces que se llama a la 
 función. A esto se le llama memorización .
- más fácil de ejecutar en paralelo.
Las funciones puras son más difíciles de escribir en algunas situaciones."""