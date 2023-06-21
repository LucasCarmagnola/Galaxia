import pygame
import colores
import disparo
import nave_enemiga
import beneficios
import tiempo
import random
from variables import *
from funciones import *

sonido_fondo.play(-1)

pygame.init()

#-----------------VENTANA-------------------------------
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Final Galaxy")

#-----------------TIMERS---------------------------------
timer_disparo_duplicado = tiempo.Timer(7000)
timer_escudo = tiempo.Timer(5000)
timer = pygame.USEREVENT 
pygame.time.set_timer(timer, 250)

crear_tabla()
while flag_game:
    lista_eventos = pygame.event.get()
    clock.tick(60)
    if jugabilidad == 0:
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag_game = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    usuario = usuario[0:-1]
                elif len(usuario) < 12:
                    usuario += evento.unicode

        #-----------------FONDO INICIO--------------------------------
        ventana.blit(fondo_inicio,(0,0))

        #------------------INGRESAR USUSARIO---------------------------  
        rect_usuario = pygame.Rect((ANCHO/2)-125, 430, 250,60)    
        pygame.draw.rect(ventana, colores.BLACK, rect_usuario, 2)
        font_input = pygame.font.SysFont("segoeuisemibold", 30)
        font_input_surface = font_input.render(usuario, True, colores.BLACK)
        ventana.blit(font_input_surface,(rect_usuario.x+20, rect_usuario.y+10))

        #-----------RECT MENSAJE INGRESAR USUARIO---------------------
        rect_nombre = pygame.draw.rect(ventana, colores.BLACK, ((ANCHO/2)-125, 360, 250,60))
        font = pygame.font.SysFont("segoeuisemibold", 20)
        texto = font.render("Ingrese su usuario:", True, colores.WHITE)
        ventana.blit(texto, (rect_nombre.x+40,rect_nombre.y+15))
        ventana.blit(marco, ((ANCHO/2)-143, 333))

        #------------------------TITULO---------------------------------
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
            foto_sonido = cargar_foto("imagenes/sonido_on.png", 40, 40)
            rect_sonido = pygame.draw.rect(ventana, colores.DODGERBLUE3, (730, 30,40,40))
            ventana.blit(foto_sonido, (rect_sonido))
            sonido_fondo.set_volume(0.2)
        else:
            foto_sonido = cargar_foto("imagenes/sonido_off.png", 40, 40)
            rect_sonido = pygame.draw.rect(ventana, colores.DODGERBLUE3, (730, 30,40,40))
            ventana.blit(foto_sonido, (rect_sonido))
            sonido_fondo.set_volume(0)
       
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if rect_jugar.collidepoint(evento.pos) and len(usuario) > 0:
                jugabilidad = 1
            if rect_sonido.collidepoint(evento.pos):
                boton_presionado = True
            if rect_puntos.collidepoint(evento.pos):
                jugabilidad = 2
                flag_puntajes = True
        elif evento.type == pygame.MOUSEBUTTONUP:
            if rect_sonido.collidepoint(evento.pos) and boton_presionado:
                flag_sonido = not flag_sonido
            boton_presionado = False

    if jugabilidad == 1:
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag_game = False
            contador_tiempo += 1
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_x and contador_tiempo > 4: 
                    sonido_disparo.play() 
                    contador_tiempo = 0        
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
        if pygame.sprite.spritecollide(nave_buena, naves_enemigas,True):
            nave_mala = nave_enemiga.NaveEnemiga(800)
            all_sprites.add(nave_mala)
            naves_enemigas.add(nave_mala)
            if beneficio_escudo == False:
                nave_buena.vida = nave_buena.vida - 1
                sonido_vida.play()

    #----------COLISIONES NAVE BUENA - VIDAS----------------
        if pygame.sprite.spritecollide(nave_buena, lista_vidas, True):
            nave_buena.vida = 3
            sonido_beneficio.play()
            vida = beneficios.Beneficio("imagenes/vida.png")
            lista_vidas.add(vida)
            all_sprites.add(vida)
    
    #----------COLISIONES NAVE BUENA - ESCUDO-------------------
        if pygame.sprite.spritecollide(nave_buena, lista_escudos, True):
            timer_escudo.start()
            sonido_beneficio.play()
            escudo = beneficios.Beneficio("imagenes/burbuja.png")
            lista_escudos.add(escudo)
            all_sprites.add(lista_escudos)
            duracion_escudo = 5
        timer_escudo.update()
        font = pygame.font.SysFont("segoeuisemibold", 25)
        texto_escudo = font.render("{0}".format(duracion_escudo), True, colores.WHITE)
        if contador_escudo > 60:
            duracion_escudo -= 1
            contador_escudo = 0
        if timer_escudo.actividad:
            beneficio_escudo = True
            contador_escudo += 1
        else: 
            beneficio_escudo = False

    #----------COLISIONES NAVE BUENA - BENEFICIO DISPARO X2----------------
        if pygame.sprite.spritecollide(nave_buena, lista_beneficio_disparos, True):
            timer_disparo_duplicado.start()
            sonido_beneficio.play()
            beneficio_disparo = beneficios.Disparos_duplicados()
            lista_beneficio_disparos.add(beneficio_disparo)
            all_sprites.add(beneficio_disparo)
        timer_disparo_duplicado.update()
        if timer_disparo_duplicado.actividad:
            beneficio = True
        else:
            beneficio = False

    #----------COLISIONES TIROS - NAVES ENEMIGAS--------------
        colisiones_bala = pygame.sprite.groupcollide(disparos, naves_enemigas, True, True)
        if colisiones_bala:
            nave_buena.score += 50
            sonido_explosion.play()
        for colision in colisiones_bala:
            nave_mala = nave_enemiga.NaveEnemiga(800)
            all_sprites.add(nave_mala)
            naves_enemigas.add(nave_mala)
    
    #----------COLISIONES NAVE BUENA - DISPAROS NAVES ENEMIGAS----------------
        if pygame.sprite.spritecollide(nave_buena, disparos_naves_enemigas, True):
            if beneficio_escudo == False:
                nave_buena.vida -= 1
                sonido_vida.play()
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
        if beneficio_escudo:
            ventana.blit(marco_vida, (nave_buena.rect.x-10, nave_buena.rect.y-22))
            ventana.blit(texto_escudo, (730, 750))

    #----------------SCORE----------------------------------
        score = nave_buena.score
        font = pygame.font.SysFont("segoeuisemibold", 25)
        texto = font.render("SCORE: {0}".format(score), True, colores.WHITE)
        ventana.blit(texto, (10,10))
        ventana.blit(marco_score, (-10,-7))

    #----------------DIBUJAR BARRA DE VIDA--------------------
        pygame.draw.rect(ventana, colores.RED1,(nave_buena.rect.x - 10,nave_buena.rect.y + 70,90,15))
        if nave_buena.vida == 3:
            pygame.draw.rect(ventana, colores.GREEN,(nave_buena.rect.x - 10,nave_buena.rect.y + 70,90,15))
        elif nave_buena.vida == 2:
            pygame.draw.rect(ventana, colores.GREEN,(nave_buena.rect.x - 10,nave_buena.rect.y + 70,60,15))
        elif nave_buena.vida == 1:
            pygame.draw.rect(ventana, colores.GREEN,(nave_buena.rect.x - 10,nave_buena.rect.y + 70,30,15))

    #---------------------GAME OVER------------------------------
        if nave_buena.vida == 0:
            jugabilidad = 2

    if jugabilidad == 2:
        if flag_tabla == 0 and len(usuario) > 0 and nave_buena.score > 0:
            commitear_tabla(usuario, nave_buena.score)
            flag_tabla = 1
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag_game = False

        #reinicio del juego
        nave_buena.vida = 3
        for nave in naves_enemigas:
            nave.reiniciar_posicion()
        vida.reiniciar_posicion()
        beneficio_disparo.reiniciar_posicion()
        escudo.reiniciar_posicion()
        timer_disparo_duplicado.actividad = False           
        all_sprites.remove(disparos_naves_enemigas, disparos)
        disparos_naves_enemigas.empty()
        disparos.empty()
        nave_buena.score = 0
        
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
                flag_tabla = 0
                flag_tabla_ordenada = 0
            if rect_puntos.collidepoint(evento.pos):
                flag_puntajes = True

        if flag_puntajes:
            ventana.blit(fondo_scores, (-100, 0))
            rect_menu_principal = pygame.draw.rect(ventana, colores.BLACK, ((ANCHO/2)-140, 650, 248,60))
            ventana.blit(marco, ((ANCHO/2)-159, 623))
            font = pygame.font.SysFont("segoeuisemibold", 17)
            texto_jugar = font.render("VOLVER AL MENU PRINCIPAL", True, colores.WHITE)
            font_titulo = pygame.font.SysFont("segoeuisemibold", 40)
            titulo = font_titulo.render("TOP 10 SCORES", True, colores.WHITE)
            ventana.blit(titulo, (250, 20))
            ventana.blit(texto_jugar, ((ANCHO/2)-132, 666))
            contador_puntos = 2

            if flag_tabla_ordenada == 0:
                lista_scores = get_scores_ordenados()
                flag_tabla_ordenada = 1

            for score in lista_scores:
                if contador_puntos < 12:
                    if len(score[1]) > 0:
                        font = pygame.font.SysFont("segoeuisemibold", 30)
                        texto_score = font.render("USUARIO: {0}   |    SCORE: {1}".format(score[1], score[2]), True, colores.WHITE)
                        ventana.blit(texto_score,(130, contador_puntos*50))
                        contador_puntos += 1

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_menu_principal.collidepoint(evento.pos):
                    jugabilidad = 0
                    flag_puntajes = False
                    flag_tabla = 0
                    flag_tabla_ordenada = 0                  
                        
    #---------------MOSTRAR CAMBIOS-----------------------
    pygame.display.flip()
    
pygame.quit()
