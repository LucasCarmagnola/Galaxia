import pygame
import random
import colores



class NaveEnemiga(pygame.sprite.Sprite):
    def __init__(self,ancho) -> None:
        super().__init__()
        self.random = random.randint(1,3)
        self.image =  pygame.image.load("nave_mala{0}.png".format(self.random))
        self.image.set_colorkey(colores.BLACK)
        self.image = pygame.transform.scale(self.image, (60,60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,ancho-60,65)
        self.rect.y = random.randrange(-1600, 0, 65)
        self.speedy = random.randint(1,3)
        self.movimientox = random.randrange(-1,2)
    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > -30:
            self.rect.x += self.movimientox
        if self.rect.top > 860 or self.rect.right < 0 or self.rect.left > 800:
            self.rect.x = random.randrange(0,800-60,65)
            self.rect.y = random.randrange(-1600, 0, 65)
            


