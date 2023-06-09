import pygame

class Timer():
    def __init__(self,duracion) -> None:
        self.duracion = duracion
        self.start_time = 0
        self.actividad = False
    def start(self):
        self.start_time = pygame.time.get_ticks()
        self.actividad = True
    def update(self):
        if self.actividad:
            tiempo_corrido = pygame.time.get_ticks() - self.start_time
            if tiempo_corrido >= self.duracion:
                self.actividad = False

