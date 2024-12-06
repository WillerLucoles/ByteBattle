import pygame
from abc import ABC, abstractmethod

from code.Const import ENTITY_SPEED , ENTITY_HEALTH


class Entity(ABC):
    def __init__(self, name: str, position: tuple, path: str = './asset/Backgrounds/Level/'):
        self.name = name
        try:
            self.surf = pygame.image.load(path + name + '.png')  # Carrega a imagem do caminho especificado
        except pygame.error as e:
            print(f"Error loading image for {name}: {e}")
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = ENTITY_SPEED
        self.health = ENTITY_HEALTH

    @abstractmethod
    def move(self, ):
        pass
