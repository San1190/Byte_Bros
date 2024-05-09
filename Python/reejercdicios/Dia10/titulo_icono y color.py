import pygame 


# Iniciar a pygame
pygame.init()

#Crear la pantalla
pantalla = pygame.display.set_mode((800,600))



#Titulo e Icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)





#Loop del juego
se_ejecuta = True
while se_ejecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
    
    pantalla.fill((205,144,228))
    pygame.display.update()


