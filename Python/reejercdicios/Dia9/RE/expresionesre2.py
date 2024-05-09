import re


import re

texto = "Llama al 546-674-4565 ya mismo"

patron = r'\d{3}-\d{3}-\d{4}'

patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
r = re.search(patron, texto)
print(r.group(1)) #solo el telf , sirvep ara dirtivir los grupos a trafes de la variavble de expresion refgular que este compliaeda

