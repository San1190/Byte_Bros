from itertools import count
import re


texto = input()
filtro = r"a|e|i|o|u"

cont = 0
for filtro in texto:
    cont+=1


print(cont)