import pygame
import colores
import nave_principal
import disparo
import nave_enemiga
import beneficios

pygame.init()

#----------------variables------------------------------
ANCHO = 800
ALTO = 800
beneficio = False


#-----------------VENTANA-------------------------------
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Intento de Galaxia piola")


#-----------------FONDO-------------------------------
fondo = pygame.image.load("fondo_estrellas_oscuro.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO,ALTO))

#-----------------TIMER---------------------------------
timer= pygame.USEREVENT 
pygame.time.set_timer(timer, 100)

#-----------------FPS---------------------------------
clock = pygame.time.Clock()

#-----------------LISTAS DE SPRITES-------------------
all_sprites = pygame.sprite.Group()
disparos = pygame.sprite.Group()
naves_enemigas = pygame.sprite.Group()
lista_vidas = pygame.sprite.Group()

#----------------NAVE PRINCIPAL-----------------------
nave_buena = nave_principal.NavePrincipal()
all_sprites.add(nave_buena)


#----------------NAVE ENEMIGA-----------------------
for i in range(20):
    nave_mala = nave_enemiga.NaveEnemiga(800)
    all_sprites.add(nave_mala)
    naves_enemigas.add(nave_mala)

for i in range(2):
    vida = beneficios.Beneficio()
    lista_vidas.add(vida)
    all_sprites.add(vida)


flag_game = True
while flag_game:
    lista_eventos = pygame.event.get()
    clock.tick(60)
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_game = False

     
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                if beneficio == False:
                    bullet = disparo.Disparo(nave_buena.rect.centerx,nave_buena.rect.y,12,23,-5)
                    disparos.add(bullet)
                    all_sprites.add(bullet)
                elif beneficio == True:
                    bullet = disparo.Disparo(nave_buena.rect.centerx-7,nave_buena.rect.y,12,23,-5)
                    bullet2 = disparo.Disparo(nave_buena.rect.centerx+7,nave_buena.rect.y,12,23,-5)
                    disparos.add(bullet)
                    all_sprites.add(bullet)
                    disparos.add(bullet2)
                    all_sprites.add(bullet2)
                
                
    all_sprites.update()

#----------COLISIONES NAVE Y NAVES ENEMIGAS---------------
    hits = pygame.sprite.spritecollide(nave_buena, naves_enemigas,True)

    choque = pygame.sprite.spritecollide(nave_buena, lista_vidas, True)
    if choque:
        nave_buena.vida = 3
    
#----------COLISIONES TIROS Y NAVES ENEMIGAS--------------
 
    for bullet in disparos:
        colisiones_bala = pygame.sprite.spritecollide(bullet, naves_enemigas, True)
        if colisiones_bala:
            bullet.colision = True         

    
    

#-----------------FONDO-------------------------------
    ventana.blit(fondo,(0,0))

#-----------------RECT NAVE PRINCIPAL-----------------
    #pygame.draw.rect(ventana, colores.GREEN, nave_buena.rect)


#----------------DIBUJAR SPRITES----------------------
    #pygame.draw.rect(ventana, colores.RED1, bullet.rect)
    all_sprites.draw(ventana)


#---------------MOSTRAR CAMBIOS-----------------------
    pygame.display.flip()

pygame.quit()
