import pygame
import colores
import nave_principal
import disparo
import nave_enemiga
import beneficios
import tiempo
import random
import variables


variables.sonido_fondo.play(-1)

pygame.init()

#----------------variables------------------------------
ANCHO = 800
ALTO = 800
beneficio = False
jugabilidad = 0
sonido = True
flag_sonido = True
y = 0


font_input = pygame.font.SysFont("segoeuisemibold", 30)
usuario = ''

#-----------------VENTANA-------------------------------
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Final Galaxy")

#-----------------FONDOS-------------------------------
fondo = pygame.image.load("fondo2.jpg").convert()
fondo = pygame.transform.scale(fondo, (ANCHO,ALTO))


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
    nave_mala = nave_enemiga.NaveEnemiga(ANCHO)
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
    if jugabilidad == 0:
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag_game = False
            if evento.type == pygame.KEYDOWN:#entrada texto ususario 
                if evento.key == pygame.K_BACKSPACE:
                    usuario = usuario[0:-1]
                else:
                    usuario += evento.unicode

        #-----------------FONDO Y MARCO--------------------------------
        fondo_inicio = pygame.image.load("fondo_inicio_tierra.jpg")
        fondo_inicio = pygame.transform.scale(fondo_inicio, (ANCHO,ALTO))
        marco = pygame.image.load("marco2.png")
        marco = pygame.transform.scale(marco, (285,115))
        ventana.blit(fondo_inicio,(0,0))

        #------------------INGRESAR USUSARIO---------------------------  
        rect_usuario = pygame.Rect((ANCHO/2)-125, 430, 250,60)    
        pygame.draw.rect(ventana, colores.BLACK, rect_usuario, 2)
        font_input_surface = font_input.render(usuario, True, colores.BLACK)
        ventana.blit(font_input_surface,(rect_usuario.x+20, rect_usuario.y+10))

        #-----------RECT MENSAJE INGRESAR USUARIO---------------------
        rect_nombre = pygame.draw.rect(ventana, colores.BLACK, ((ANCHO/2)-125, 360, 250,60))
        font = pygame.font.SysFont("segoeuisemibold", 20)
        texto = font.render("Ingrese su usuario:", True, colores.WHITE)
        ventana.blit(texto, (rect_nombre.x+40,rect_nombre.y+15))
        ventana.blit(marco, ((ANCHO/2)-143, 333))

        #------------------------TITULO---------------------------------
        marco2 = pygame.image.load("marco2.png")
        marco2 = pygame.transform.scale(marco2, (420,185))
        font = pygame.font.SysFont("Arial", 60)
        titulo = font.render("Final Galaxy", True, colores.WHITE)
        ventana.blit(titulo, ((ANCHO/2)-160,50))
        ventana.blit(marco2, ((ANCHO/2)-205, -8))

        #----------------------RECT JUGAR------------------------------
        rect_jugar = pygame.draw.rect(ventana, colores.BLACK, ((ANCHO/2)-125, 230, 250,60))
        font = pygame.font.SysFont("segoeuisemibold", 40)
        texto = font.render("JUGAR", True, colores.WHITE)
        ventana.blit(texto, (rect_jugar.x+60,rect_jugar.y))
        ventana.blit(marco, ((ANCHO/2)-141, 200))

        #-------------------RECT MOSTRAR PUNTOS------------------------
        rect_puntos = pygame.draw.rect(ventana, colores.BLACK, ((ANCHO/2)-125, 550, 250,60))
        font = pygame.font.SysFont("segoeuisemibold", 20)
        texto = font.render("Mostrar puntajes record", True, colores.WHITE)
        ventana.blit(texto, (rect_puntos.x+17,rect_puntos.y+15))
        ventana.blit(marco, ((ANCHO/2)-142, 522))

        #-------------------RECT SONIDO--------------------------------
        
        if flag_sonido:
            foto_sonido = pygame.image.load("sonido_on.png")
            foto_sonido = pygame.transform.scale(foto_sonido, (40,40))
            rect_sonido = pygame.draw.rect(ventana, colores.DODGERBLUE3, (730, 30,40,40))
            ventana.blit(foto_sonido, (rect_sonido))
        else:
            foto_sonido = pygame.image.load("sonido_off.png")
            foto_sonido = pygame.transform.scale(foto_sonido, (40,40))
            rect_sonido = pygame.draw.rect(ventana, colores.DODGERBLUE3, (730, 30,40,40))
            ventana.blit(foto_sonido, (rect_sonido))

        if sonido == True:
            variables.sonido_fondo.set_volume(0.2)
        elif sonido == False:
            variables.sonido_fondo.set_volume(0)
      
        if evento.type == pygame.MOUSEBUTTONDOWN :
            if rect_jugar.collidepoint(evento.pos) and usuario.isalnum():
                jugabilidad = 1
            if rect_sonido.collidepoint(evento.pos) and flag_sonido:
                sonido = False
                flag_sonido = False
            elif rect_sonido.collidepoint(evento.pos) and flag_sonido == False:
                sonido = True
                flag_sonido = True
    
            '''if rect_puntos.collidepoint(evento.pos):
                jugabilidad = 2'''

    #hacer un try y except
    if jugabilidad == 1:
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag_game = False
        
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_x: 
                    variables.sonido_disparo.play()            
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

                        
        #---------------DISPAROS NAVES ENEMIGAS----------------
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
            variables.sonido_vida.play()

    #----------COLISIONES NAVE BUENA - VIDAS----------------
        choque = pygame.sprite.spritecollide(nave_buena, lista_vidas, True)
        if choque:
            nave_buena.vida = 3
            variables.sonido_beneficio.play()
        for e_choque in choque:
            vida = beneficios.Beneficio()
            lista_vidas.add(vida)
            all_sprites.add(vida)

    #----------COLISIONES NAVE BUENA - BENEFICIO DISPARO X2----------------
        interseccion = pygame.sprite.spritecollide(nave_buena, lista_beneficio_disparos, True)
        if interseccion:
            timer_disparo_duplicado.start()
            variables.sonido_beneficio.play()
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
            nave_buena.score += 50
            variables.sonido_explosion.play()
        for colision in colisiones_bala:
            nave_mala = nave_enemiga.NaveEnemiga(800)
            all_sprites.add(nave_mala)
            naves_enemigas.add(nave_mala)
    

    #----------COLISIONES NAVE BUENA - DISPAROS NAVES ENEMIGAS----------------
        colision_disparo_enemigo = pygame.sprite.spritecollide(nave_buena, disparos_naves_enemigas, True)
        if colision_disparo_enemigo:
            nave_buena.vida -= 1
            variables.sonido_vida.play()
        for colision in colision_disparo_enemigo:
            nave_ataque = random.choice(naves_enemigas.sprites())
            disparo_nave = disparo.Disparo(nave_ataque.rect.centerx,nave_ataque.rect.bottom,12,23,4)
            disparos_naves_enemigas.add(disparo_nave)
            all_sprites.add(disparo_nave)
        
    #-----------------FONDO-------------------------------
        
        y_relativa = y % fondo.get_rect().height
        ventana.blit(fondo,(0,y_relativa - fondo.get_rect().height))
        if y_relativa < ALTO:
            ventana.blit(fondo, (0, y_relativa))
        y += 1

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

    #---------------GAME OVER------------------------------
        if nave_buena.vida < 1:
            #jugabilidad = 2
        #if jugabilidad == 2:
            variables.sonido_disparo.stop()
            variables.sonido_explosion.stop()
            variables.sonido_vida.stop()
            for evento in lista_eventos:
                if evento.type == pygame.QUIT:
                    flag_game = False
            nave_buena.score = 0
            all_sprites.remove(disparos)
            fondo_game_over = pygame.image.load("fondo_gameover.jpg")
            fondo_game_over = pygame.transform.scale(fondo_game_over, (ANCHO+400,ALTO))
            marco = pygame.image.load("marco2.png")
            marco = pygame.transform.scale(marco, (287,115))
            ventana.blit(fondo_game_over,(-200,0))
            #-------------------RECT JUGAR------------------------------
            rect_jugar = pygame.draw.rect(ventana, colores.BLACK, ((ANCHO/2)-125, 200, 250,60))
            font = pygame.font.SysFont("segoeuisemibold", 25)
            texto_jugar = font.render("JUGAR DENUEVO", True, colores.WHITE)
            ventana.blit(texto_jugar, (rect_jugar.x+25,rect_jugar.y+10))
            #-------------------RECT MOSTRAR PUNTOS------------------------------ 
            rect_puntos = pygame.draw.rect(ventana, colores.BLACK, ((ANCHO/2)-125, 500, 250,60))
            font = pygame.font.SysFont("segoeuisemibold", 20)
            texto_puntos = font.render("Mostrar puntajes record", True, colores.WHITE)
            ventana.blit(texto_puntos, (rect_puntos.x+17,rect_puntos.y+15))
            #-------------------GAME OVER MENSAJE------------------------------
            font = pygame.font.SysFont("segoeuisemibold", 50)
            texto_gameover = font.render("GAME OVER", True, colores.WHITE)
            ventana.blit(texto_gameover, ((ANCHO/2)-140,50))
            ventana.blit(marco, ((ANCHO/2)-144, 170))
            ventana.blit(marco, ((ANCHO/2)-144, 470))

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_jugar.collidepoint(evento.pos):
                    jugabilidad = 1
                    nave_buena.vida = 3
                    nave_buena.score = 0
                    for nave in naves_enemigas:
                        nave.reiniciar_posicion()
                    vida.reiniciar_posicion()
                    beneficio_disparo.reiniciar_posicion()
                    all_sprites.remove(disparos_naves_enemigas, disparos)
                    disparos_naves_enemigas.empty()
                    disparos.empty()
                    
  
            #---------------MOSTRAR CAMBIOS-----------------------
    pygame.display.flip()
    

pygame.quit()
