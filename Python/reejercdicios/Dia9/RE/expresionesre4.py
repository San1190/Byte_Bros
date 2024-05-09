import re

t = "No atendemos los martes por la tarde"

p = r'lunes|martes'

b = re.search(p , t)
print(b)

