from pathlib import Path


base =Path.home() #=> de donde viene , la instancia ocn la ruta absoluta al directorio princiopa
guia = Path(base ,"Europa", "España",Path("Barcelona","Sagrada_Familia.txt"))#.txt

guia2 = guia.with_name("La_Pedrera.txt")

print(guia.parent)#ruta relativa/// parent : lleva al anterior Bareclona => España =>Europa
print(guia2)

guia3 = Path(Path.home(),"Europa")

for txt in Path(guia3).glob("*.txt"): # // **/*.txt => para todo
    print(txt)


guia4 = Path("Europa","españa","Barcelona", "Sagrada_Familia.txt") # desde puntos en particular
en_europa = guia4.relative_to(Path("Europa"))
en_espania = guia4.relative_to(Path("Europa","España"))

print(en_europa)
print(en_espania)



