import pygame
import colores
import random 

class Beneficio(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image =  pygame.image.load("vida.png")
        self.image.set_colorkey(colores.BLACK)
        self.image = pygame.transform.scale(self.image, (60,60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,740, 200)
        self.rect.y = random.randrange(-8000, -2000, 5000)
    def update(self):
        self.rect.y += 2
        if self.rect.top > 860:
            self.rect.x = random.randrange(0,740,200)
            self.rect.y = random.randrange(-8000, -2000, 5000)
