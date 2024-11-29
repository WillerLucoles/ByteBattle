import pygame
from code.Entity import Entity

class Player(Entity):
    def __init__(self, name: str, position: tuple, controls: dict, speed: int = 5):
        super().__init__(name, position, path='../asset/Players/')
        self.speed = speed
        self.controls = controls  # Define os controles personalizados para o Player

    def move(self):
        """Atualiza a posição do Player com base nas teclas pressionadas."""
        pressed_key = pygame.key.get_pressed()

        # Movimento vertical
        if pressed_key[self.controls['up']]:
            self.rect.centery -= self.speed
        if pressed_key[self.controls['down']]:
            self.rect.centery += self.speed

        # Movimento horizontal
        if pressed_key[self.controls['left']]:
            self.rect.centerx -= self.speed
        if pressed_key[self.controls['right']]:
            self.rect.centerx += self.speed

        # Limitar o Player para que não saia da tela
        self.rect.clamp_ip(pygame.Rect(0, 0, 576, 354))  # Substitua os valores pelo tamanho da sua janela
