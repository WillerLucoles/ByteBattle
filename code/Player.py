import pygame

from code.Const import WIN_WIDTH , WIN_HEIGHT
from code.Entity import Entity

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position, path='../asset/Players/')
        self.speed = 5  # Velocidade do Player


    def move(self):

        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP]:
            self.rect.centery -= self.speed
        if pressed_key[pygame.K_DOWN]:
            self.rect.centery += self.speed
        if pressed_key[pygame.K_LEFT]:
            self.rect.centerx -= self.speed
        if pressed_key[pygame.K_RIGHT]:
            self.rect.centerx += self.speed


        self.rect.clamp_ip(pygame.Rect(0, 0, WIN_WIDTH, WIN_HEIGHT))
