class Humano:
    def __init__(self,edad):
       # self.edad = 25
        self.edad = edad

    def hablar(self,mensaje):
       # print (self.edad)
        print(mensaje)
    

class IngSistemas(Humano):
    def __init__(self):
        print("Hola")

    def programar(self,lenguaje):
        print("Voy a programar en ",lenguaje)


class LicDerecho(Humano):
    def __init__(self,escuela):
        print("Lic. en derecho en :",escuela)
    def estudiarCaso(self,de):
        print("Debo estudiar el caso de", de)



class Estudioso(IngSistemas,LicDerecho): #segun el orden varia el metodo innit, es decir, si ambos tienes coje el primero

    pass



pedro = IngSistemas()
raul = LicDerecho(27)

pepe = Estudioso()

pepe.hablar("Hola, soy de herencia multiple")
pepe.programar("C++")
pepe.estudiarCaso("Juan")

pedro.programar('Python')
raul.estudiarCaso('Pedro')

'''
print('Soy Pedro y tengo',pedro.edad)
print('Soy Raul y tengo', raul.edad)
pedro.hablar('Hola')
'''
pedro.hablar("Hola")
raul.hablar('Hola pedro')