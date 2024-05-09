import shutil

carpeta = " Aqui va el directorio de la carpeta"

archivo_destino = "Aqui el nombre del archivo"

shutil.make_archive(archivo_destino, "zip" ,carpeta)

shutil.unpack_archive("nombrearchivo.zip","Donde se guarda nobmre carpeta")