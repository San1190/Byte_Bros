import pygame 

pygame.init()


pantalla = pygame.display.set_mode((800,600))

se_ejecuta = True
while se_ejecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
