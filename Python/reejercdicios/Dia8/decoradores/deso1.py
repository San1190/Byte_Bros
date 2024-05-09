#funciones que modifican otras funciones

def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adios")
    return otra_funcion

#@decorar_saludo
def mayuscula(texto):
    print(texto.upper())


@decorar_saludo
def minuscula(texto):
    print(texto.lower())


mayuscula_decorada = decorar_saludo(mayuscula)

mayuscula("fede")
mayuscula_decorada("fede")



