import os
import shutil
import send2trash
#shutil.move("curso.txt", "C:\\\\Users\\\\sanfu\\\\Desktop\\\\python\\\\reejercdicios\\\\Dia9\\\\os y shutil")

send2trash.send2trash('curso.txt')
#eliminar archivos ( unlink , rmdir(carpeta vacia) ,shutil(rmtree) elimina todo lo de la ruta / no se usa )