'''metodos de instancia (los clasicos)
metodos de clase (@classmethod) --- self = cls
metodos estáticos(@staticmethod)--- self == nada'''


class Pajaro():
    
    alas = True

    def __init__(self ,color, espcecie): #constructor de la clase
        self.color = color
        self.especie = espcecie

    def piar(self):
        print('Pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()

    def pinar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es {self.color}')

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        #print(f'Es de color {self.color}') ==> Error
        cls.alas = False
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        print("El pajaro mira")



Pajaro.mirar()

    


Pajaro.poner_huevos(3)

piolin = Pajaro('amarillo','canario')


piolin.volar(16)
piolin.pinar_negro()

piolin.alas = False
print(piolin.alas)