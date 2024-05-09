class Animal():

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color


    def nacer(self):
        print("Este animal ha nacido")




class Pajaro(Animal):
    pass



piolin = Pajaro(2, 'amarillo')

print(piolin.color)

#print(Pajaro.__bases__)# para ver de quien hereda
#print(Animal.__subclasses__)