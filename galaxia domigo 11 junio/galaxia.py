import pygame
import colores
import nave_principal
import disparo
import nave_enemiga
import beneficios
import tiempo
import random

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

fondo_score = pygame.image.load("luna_150.png")
fondo_score = pygame.transform.scale(fondo_score, (160,160))

#-----------------TIMER---------------------------------
timer_disparo_duplicado = tiempo.Timer(7000)


timer = pygame.USEREVENT 
pygame.time.set_timer(timer, 250)


#-----------------FPS---------------------------------
clock = pygame.time.Clock()

#-----------------LISTAS DE SPRITES-------------------
all_sprites = pygame.sprite.Group()
disparos = pygame.sprite.Group()
naves_enemigas = pygame.sprite.Group()
lista_vidas = pygame.sprite.Group()
lista_beneficio_disparos = pygame.sprite.Group()
disparos_naves_enemigas = pygame.sprite.Group()

#----------------NAVE PRINCIPAL-----------------------
nave_buena = nave_principal.NavePrincipal()
all_sprites.add(nave_buena)


#----------------NAVE ENEMIGA-----------------------
for i in range(35):
    nave_mala = nave_enemiga.NaveEnemiga(800)
    all_sprites.add(nave_mala)
    naves_enemigas.add(nave_mala)


#----------------VIDA-----------------------
vida = beneficios.Beneficio()
lista_vidas.add(vida)
all_sprites.add(vida)

#----------------DISPAROS X2-----------------------
beneficio_disparo = beneficios.Disparos_duplicados()
lista_beneficio_disparos.add(beneficio_disparo)
all_sprites.add(beneficio_disparo)



flag_game = True
while flag_game:
    lista_eventos = pygame.event.get()
    clock.tick(60)
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_game = False
     
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_x:             
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

                       
    #---------------DISPAROS NAVE ENEMIGA----------------
        if evento.type == pygame.USEREVENT:
            if evento.type == timer and len(disparos_naves_enemigas) < 100:
                nave_ataque = random.choice(naves_enemigas.sprites())
                if nave_ataque.rect.x > 0 and nave_ataque.rect.x < 800:
                    disparo_nave = disparo.Disparo(nave_ataque.rect.centerx,nave_ataque.rect.bottom,12,23,5)
                    disparos_naves_enemigas.add(disparo_nave)
                    all_sprites.add(disparo_nave)
                
                
    all_sprites.update()

#----------COLISIONES NAVE BUENA - NAVES ENEMIGAS----------------
    hits = pygame.sprite.spritecollide(nave_buena, naves_enemigas,True)
    for hit in hits:
        nave_mala = nave_enemiga.NaveEnemiga(800)
        all_sprites.add(nave_mala)
        naves_enemigas.add(nave_mala)
    if hits:
        nave_buena.vida = nave_buena.vida - 1

#----------COLISIONES NAVE BUENA - VIDAS----------------
    choque = pygame.sprite.spritecollide(nave_buena, lista_vidas, True)
    if choque:
        nave_buena.vida = 3
    for e_choque in choque:
        vida = beneficios.Beneficio()
        lista_vidas.add(vida)
        all_sprites.add(vida)

#----------COLISIONES NAVE BUENA - DISPARO X2----------------
    interseccion = pygame.sprite.spritecollide(nave_buena, lista_beneficio_disparos, True)
    if interseccion:
        timer_disparo_duplicado.start()
    timer_disparo_duplicado.update()
    if timer_disparo_duplicado.actividad:
        beneficio = True
    else:
        beneficio = False
    for e_interseccion in interseccion:
        beneficio_disparo = beneficios.Disparos_duplicados()
        lista_beneficio_disparos.add(beneficio_disparo)
        all_sprites.add(beneficio_disparo)
    
#----------COLISIONES TIROS - NAVES ENEMIGAS--------------
    colisiones_bala = pygame.sprite.groupcollide(disparos, naves_enemigas, True, True)
    if colisiones_bala:
        nave_buena.score += 100
    for colision in colisiones_bala:
        nave_mala = nave_enemiga.NaveEnemiga(800)
        all_sprites.add(nave_mala)
        naves_enemigas.add(nave_mala)

#----------COLISIONES NAVE BUENA - DISPAROS NAVES ENEMIGAS----------------
    colision_disparo_enemigo = pygame.sprite.spritecollide(nave_buena, disparos_naves_enemigas, True)
    if colision_disparo_enemigo:
        nave_buena.vida -= 1
    for colision in colision_disparo_enemigo:
        nave_ataque = random.choice(naves_enemigas.sprites())
        disparo_nave = disparo.Disparo(nave_ataque.rect.centerx,nave_ataque.rect.bottom,12,23,4)
        disparos_naves_enemigas.add(disparo_nave)
        all_sprites.add(disparo_nave)
    
#-----------------FONDO-------------------------------
    ventana.blit(fondo,(0,0))
    ventana.blit(fondo_score, (0,5))

#----------------DIBUJAR SPRITES----------------------
    all_sprites.draw(ventana)

#----------------SCORE-------------------------------
    score = nave_buena.score
    font = pygame.font.SysFont("segoeuisemibold", 25)
    texto = font.render("SCORE: {0}".format(score), True, colores.WHITE)
    ventana.blit(texto, (10,10))

#----------------DIBUJAR BARRA DE VIDA----------------
    pygame.draw.rect(ventana, colores.RED1,(nave_buena.rect.x - 10,nave_buena.rect.y + 70,90,15))
    if nave_buena.vida == 3:
        pygame.draw.rect(ventana, colores.GREEN,(nave_buena.rect.x - 10,nave_buena.rect.y + 70,90,15))
    elif nave_buena.vida == 2:
        pygame.draw.rect(ventana, colores.GREEN,(nave_buena.rect.x - 10,nave_buena.rect.y + 70,60,15))
    elif nave_buena.vida == 1:
        pygame.draw.rect(ventana, colores.GREEN,(nave_buena.rect.x - 10,nave_buena.rect.y + 70,30,15))

#---------------MOSTRAR CAMBIOS-----------------------
    pygame.display.flip()

pygame.quit()
