
import pygame 
import random
import math
from pygame import mixer

# Iniciar a pygame
pygame.init()

#Crear la pantalla
pantalla = pygame.display.set_mode((800,600))



#Titulo e Icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

fondo = pygame.image.load("Fondo.jpg")

#Musica
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)


# variables del Jugador
img_jugador = pygame.image.load("nave-espacial.png")
jugador_x = 368     #400 - 32 la mitad del ancho 
jugador_y = 500    #600 - 64
jugador_x_cambio = 0



# variables del enemigo
img_enemigo = []
enemigo_x = []    
enemigo_y = []   
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png")) 
    enemigo_x.append(random.randint(0, 736))   #400 - 32 la mitad del ancho 
    enemigo_y.append(random.randint(50, 200))       #600 - 64
    enemigo_x_cambio.append(0.2)  
    enemigo_y_cambio.append(50)  



# variables de la bala
img_bala = pygame.image.load("bala.png")
bala_x = 0   #400 - 32 la mitad del ancho 
bala_y = 500    #600 - 64
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False

#puntuacion
puntuacion = 0
fuente = pygame.font.Font("abuse.ttf", 32)
texto_x = 10
texto_y = 10


#Texto final de juego
fuente_final = pygame.font.Font("abuse.ttf", 40)

def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (60 , 200))


#funcion mostrar puntuacion
def mostrar_puntuacion(x, y):
    texto = fuente.render(f"Puntuacion: {puntuacion}", True, (255,255,255))
    pantalla.blit(texto, (x, y))

    


#Funcion jugador
def jugador(x, y):

    pantalla.blit(img_jugador, (x, y))


#Funcion enemigo
def enemigo(x, y, ene):

    pantalla.blit(img_enemigo[ene], (x, y))


#Funcion dispara bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))

#Fucion detectar colisiones

def colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_2 - x_1 , 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27 :
        return True
    else:
        return False




#Loop del juego
se_ejecuta = True
while se_ejecuta:
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        #Mover jugador
        if evento.type == pygame.KEYDOWN:
           
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.4
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.4
            #Disparar bala
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("disparo.mp3")
                
                if not bala_visible:
                    sonido_bala.play()
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        #Parar jugador
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = 0
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
        

           

    #imagen
    #pantalla.fill((205,144,228))
    pantalla.blit(fondo, (0, 0))
    #Modificar ubicacion
    jugador_x += jugador_x_cambio
    #Mantener dentro de bordes jugador
    if jugador_x <= 0:
        jugador_x = 0

    if jugador_x >= 736:
        jugador_x = 736

    #Modificar ubicacion enemigo
    for e in range(cantidad_enemigos):

        #fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            
            texto_final()
            break



        enemigo_x[e] += enemigo_x_cambio[e]

           #Mantener dentro de bordes enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.2
            enemigo_y[e] += enemigo_y_cambio[e]

        elif enemigo_x[e]>= 736:
            enemigo_x_cambio[e] = -0.2
            enemigo_y[e] += enemigo_y_cambio[e]



         #colision
        colision1 = colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y) 
        if colision1:
            sonido_colision = mixer.Sound("golpe.mp3")
            sonido_colision.set_volume(0.3)
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntuacion += 1 
            print(puntuacion)
            enemigo_x[e] = random.randint(0, 736)     
            enemigo_y[e] = random.randint(50, 200)



        enemigo(enemigo_x[e], enemigo_y[e], e)

    #movimiento bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x,bala_y)
        bala_y -= bala_y_cambio


    




    
    jugador(jugador_x, jugador_y)


    mostrar_puntuacion(texto_x, texto_y)

    #Actualizar
    pygame.display.update()

    


