from collections import namedtuple

mi_tupla = (500, 18, 65)

print(mi_tupla[1])

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])

ariel = Persona('Ariel', 1.76, 79)

print(ariel.altura)

print(ariel[2])