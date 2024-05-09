from pathlib import Path

carpeta = Path('/Users/sanfu/Desktop/alternativa')

archivo = carpeta / 'otro_archivo.txt'

mi_archivo = open(archivo)

print(mi_archivo.read()) #para quer cualquier usuario pueda abrir archivo