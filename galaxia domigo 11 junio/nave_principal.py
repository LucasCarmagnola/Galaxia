import pygame
import colores
#import galaxia



class NavePrincipal(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("nave_espacial3.png")
        self.image = pygame.transform.scale(self.image, (70,70))
        self.rect = self.image.get_rect()
        self.rect.centery = 740
        self.rect.centerx = 400
        self.vida = 3
        self.score = 0
    def update(self):
        lista_teclas = pygame.key.get_pressed()
        if lista_teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= 6
        if lista_teclas[pygame.K_RIGHT] and self.rect.right < 800:          
            self.rect.centerx += 6


    

   
        




