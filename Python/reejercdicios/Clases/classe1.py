class Pajaro:
    pass #vacio

mi_pajaro = Pajaro()
otro_pajaro = Pajaro()
#print(type(mi_pajaro))
print(mi_pajaro)
print(otro_pajaro)

# esto es una clase basica, lo habras visto en w3s , tiene esa estructura

class Perro:
    #aqui irian los atributos de la clase(las variables q quieres q tengas) pero primero tienes q hacer el metodo de los atributos, el
    #__init__
    '''aqui coloco el pass para q no de error. se colocan los valores q quieres q tenga las cosas de la clase
    por ejemplo el color y la piel o ns. Las clases sbs para q sirven=?'''


    #esto es como el metodo general donde defines los argumentos
    def __init__(self,color, raza,tamaño) :
        self.color = color
        self.raza = raza
        self.tamaño = tamaño

    def EspecificacionesDelPutoMamon(self):
        print(f'''Tu perro de mierda es de color: {self.color} , de raza asquerosa: {self.raza} y el tamaño del gordo es: {self.tamaño}''')

    #esto es como un equals, ns una funcion cualquiera.
    def Salto(self, salto):
        print(f"Tu perro, {self.raza}, salta {salto}.mts")

    def Raza(self, raza):
        print("Tu perro es de raza: " + raza)


#aqui defines tu perro con sus parametros en este caso solo el color.
perro1 = Perro("Rojo", "Pastor ESPAÑOL", 234)

perro1.EspecificacionesDelPutoMamon()
perro1.Salto(23)
#una vez definido puedes llamar a sus metodos con su nombre y punto (como el ti.toString() por ejemplo)

#perro1.Color() #aqui no hace falta q coloques nada entrew parenteriso porque en esa funcion no se necesita nada de entrada
#lo del self es parecido al this, todos los atributos tienen q estar asi, te lo comparo con java si quieres

#perro2 = Perro("Marrón") # el color es algo comun a todos los perros por eso siempre q crees uno hara falta ,
#en verd la raza tmb pero me la pela de auqi a japon


# voy a hacer bien una clase pa q entiendas los atributos globales y especificos se llaman