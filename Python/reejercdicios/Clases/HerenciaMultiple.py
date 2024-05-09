from os import system


class Padre:
    def hablar(sef):
        print("Hola")


class Madre:
    def reir(self):
        print("AJAJAJAJJAAJ")

    def hablar(self):
        print("Que tal")

class Hijo(Padre, Madre): # orden de herencia  cuando se repite el metodo
    pass

class Nieto(Hijo):
    pass


mi_nieto = Nieto()
system('cls')
mi_nieto.hablar()
mi_nieto.reir()

print(Nieto.__mro__)