mi_lista = [1,1,1,1,1,1,1,1,1,1]

print(len(mi_lista))

class CD:

    def __init__(self, autor, titulo, cantidad):
        self.autor = autor
        self.titulo = titulo
        self.cantidad =  cantidad
    
    def __str__(self):
        return f"Albun: {self.titulo} de {self.autor}"

    def __len__(self):
        return self.cantidad

    def __del__(self):
        print( "Se ha elimininado el CD")


        


mi_cd = CD('Pink Floyd', 'The Wall', 24)


print(mi_cd)

print(len(mi_cd))

del mi_cd

