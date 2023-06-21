import pygame
from funciones import *
import nave_principal
import beneficios

ANCHO = 800
ALTO = 800
beneficio = False
jugabilidad = 0
flag_sonido = True
y = 0
usuario = ''
data_base = False
flag_puntajes = False
game_over = False
flag_tabla = 0
flag_tabla_ordenada = 0
contador_tiempo = 0
boton_presionado = False
beneficio_escudo = False
duracion_escudo = 5
contador_escudo = 0


#------------------grupos de sprites-------------------
all_sprites = pygame.sprite.Group()
disparos = pygame.sprite.Group()
naves_enemigas = pygame.sprite.Group()
lista_vidas = pygame.sprite.Group()
lista_beneficio_disparos = pygame.sprite.Group()
disparos_naves_enemigas = pygame.sprite.Group()
lista_escudos = pygame.sprite.Group()


#----------------------fps---------------------------------
clock = pygame.time.Clock()

#------------------NAVE PRINCIPAL-----------------------
nave_buena = nave_principal.NavePrincipal()
all_sprites.add(nave_buena)

#----------------VIDA------------------------------
vida = beneficios.Beneficio("imagenes/vida.png")
lista_vidas.add(vida)
all_sprites.add(vida)

#----------------DISPAROS X2-----------------------------
beneficio_disparo = beneficios.Disparos_duplicados()
lista_beneficio_disparos.add(beneficio_disparo)
all_sprites.add(beneficio_disparo)

#------------------ESCUDO------------------------------
escudo = beneficios.Beneficio("imagenes/burbuja.png")
lista_escudos.add(escudo)
all_sprites.add(lista_escudos)

#----------------------imagenes-----------------------------------
fondo = cargar_foto("imagenes/fondo2.jpg", ANCHO, ALTO)
fondo_game_over = cargar_foto("imagenes/fondo_gameover.jpg", ANCHO+400, ALTO)
marco = cargar_foto("imagenes/marco2.png", 287, 115)
fondo_scores = cargar_foto("imagenes/fondo_scores.jpg", ANCHO+200, ALTO)

#-----------------FONDO Y MARCO--------------------------------
fondo_inicio = cargar_foto("imagenes/fondo_inicio_tierra.jpg", ANCHO, ALTO)
marco = cargar_foto("imagenes/marco2.png", 285, 115)
marco2 = cargar_foto("imagenes/marco2.png", 420, 185)
marco_score = cargar_foto("imagenes/marco2.png", 210, 70)
marco_vida = cargar_foto("imagenes/marco2.png", 90, 120)


#--------------------SONIDOS----------------------------------------
pygame.mixer.init()
sonido_fondo = pygame.mixer.Sound("sonidos/nuevo_fondo.mp3")
sonido_disparo = pygame.mixer.Sound("sonidos/disparo_laser.wav")
sonido_explosion = pygame.mixer.Sound("sonidos/sonido_explosion.wav")
sonido_vida = pygame.mixer.Sound("sonidos/perder_vida.wav")
sonido_beneficio = pygame.mixer.Sound("sonidos/beneficio.mp3")
sonido_disparo.set_volume(0.05)
sonido_fondo.set_volume(0.2)
sonido_explosion.set_volume(0.05)
sonido_vida.set_volume(5)
sonido_beneficio.set_volume(6)