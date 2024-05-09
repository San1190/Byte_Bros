import os


#if archo.startswith("2015")

#print(os.walk("C:\\Users\\sanfu\\Desktop\\python\\reejercdicios\\Dia9\\os y shutil"))

ruta = "C:\\Users\\sanfu\\Desktop\\python"

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"En la carpeta: {carpeta}")
    print(f"Las subcarpetas son:")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print("Los archivos son:")
    for a in archivo:
        print(f"\t{a}")
    print("\n")
  