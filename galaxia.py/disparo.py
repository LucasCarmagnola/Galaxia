import pygame
import colores



class Disparo(pygame.sprite.Sprite):
    def __init__(self,x,y,ancho,alto,movimiento) -> None:
        super().__init__()
        self.image = pygame.image.load("disparo.png")
        self.image.set_colorkey(colores.BLACK)
        self.image = pygame.transform.scale(self.image,(ancho,alto))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.centerx = x
        self.speedy = movimiento
        self.visibilidad = True
        self.colision = False
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0 or self.colision == True:
            self.kill()
    




