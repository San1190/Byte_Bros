#atriibutos de instancia

class Pajaro():
    #atributo de clase
    alas = True

    def __init__(self,color,espcecie): #constructor de la clase
        self.color = color
        self.especie = espcecie


mi_pajaro =Pajaro('negro','Tucán')

palabra = 'hola'

print(mi_pajaro.color)
print(mi_pajaro.especie)
print(mi_pajaro.alas)