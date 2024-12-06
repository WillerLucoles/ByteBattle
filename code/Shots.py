import pygame
from code.Entity import Entity


class Shot(Entity):
    def __init__(self, name: str, position: tuple, speed: int, direction: int, path: str = './asset/Shots/'):
        """
        Cria um tiro no jogo.
        :param name: Nome do sprite do tiro.
        :param position: Posição inicial (x, y).
        :param speed: Velocidade do tiro.
        :param direction: Direção do movimento (-1 para cima, 1 para baixo).
        :param path: Caminho do sprite.
        """
        super().__init__(name, position, path)
        self.speed = speed
        self.direction = direction  # -1 para cima, 1 para baixo

    def move(self):
        """Atualiza a posição do tiro."""
        self.rect.x += self.speed * self.direction

        # Remove o tiro se sair da tela
        if self.rect.right < 0 or self.rect.left > pygame.display.get_surface().get_width():
            self.health = 0  # Marca como 'morto'
