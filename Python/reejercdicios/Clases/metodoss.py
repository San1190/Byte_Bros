class Pajaro():
    
    alas = True

    def __init__(self ,color, espcecie): #constructor de la clase
        self.color = color
        self.especie = espcecie

    def piar(self):
        print('Pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")


piolin = Pajaro('amarillo','canario')

piolin.piar()

piolin.volar(16)

