import re

achivo = open("polla.txt" , 'r+')

texto = achivo.readlines() // '82304832490823490238902384'

texto = "Llama al 546-674-4565 ya mismo"

#crear un patron para filtrar unos datos en un documento o texcto o direcoi o pagina weer


patron = r'\d{3}-\d{3}-\d{4}'

patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
r = re.search(patron, texto)
# solo el telf , sirvep ara dirtivir los grupos a trafes de la variavble de expresion refgular que este compliaeda
print(r.group(1))
