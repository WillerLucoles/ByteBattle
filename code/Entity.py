import pygame
from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        #print(f"Creating entity: {name}, at position: {position}") teste posicao de imagem
        self.name = name
        try:
            self.surf = pygame.image.load('../asset/Backgrounds/Level/' + name + '.png')
           # print(f"Image loaded for {name}") teste imagem carregada
        except pygame.error as e:
            print(f"Error loading image for {name}: {e}")
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self):
        pass
