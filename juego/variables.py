import pygame

pygame.mixer.init()
sonido_fondo = pygame.mixer.Sound("nuevo_fondo.mp3")
sonido_disparo = pygame.mixer.Sound("disparo_laser.wav")
sonido_explosion = pygame.mixer.Sound("sonido_explosion.wav")
sonido_vida = pygame.mixer.Sound("perder_vida.wav")
sonido_beneficio = pygame.mixer.Sound("beneficio.mp3")
sonido_disparo.set_volume(0.05)
sonido_fondo.set_volume(0.2)
sonido_explosion.set_volume(0.05)
sonido_vida.set_volume(5)
sonido_beneficio.set_volume(6)