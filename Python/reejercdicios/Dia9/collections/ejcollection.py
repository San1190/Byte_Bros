from collections import deque
from typing import Deque

lista_paises = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]
pais = deque(lista_paises)
p = input("Ingresa un país: ")
pais.appendleft(p)

print(pais)
