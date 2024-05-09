import re
t = "No atendemos los jueves por la tarde"

#b = re.search(r'.{4}demos',t)
b = re.search(r'^\D$',t)

b = re.findall(r'[^\s]+',t)
print(''.join(b))