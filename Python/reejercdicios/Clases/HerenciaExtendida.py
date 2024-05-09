from this import d
from turtle import color


class Animal():

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color


    def nacer(self):
        print("Este animal ha nacido")
    
    def hablar(self):
        print("Este animal emite un sonido")





class Pajaro(Animal):
    
    def __init__(self, edad, color, altura):
        super().__init__(edad,color)
        #self.edad = edad
        #self.color = color
        self.altura = altura

    def hablar(self):#se sobreescribe
        print("pio")

    def volar(self, metros):
        print(f"El pajaro vuelta {metros} metros")



piolin = Pajaro(2, 'amarillo', 60)

mi_animal = Animal(23, 'negro')
piolin.nacer()
piolin.hablar()

piolin.volar(100)
