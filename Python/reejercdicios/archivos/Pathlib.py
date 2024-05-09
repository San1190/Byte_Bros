from pathlib import Path,PureWindowsPath

carpeta = Path('/Users/sanfu/Desktop/alternativa/otro_archivo.txt')

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)
#archivo = carpeta / 'otro_archivo.txt'

print(carpeta.read_text())

print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Existe")

