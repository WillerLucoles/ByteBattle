import pygame

from code.Const import WIN_WIDTH , WIN_HEIGHT , SHOT_SPRITES , ENTITY_HEALTH
from code.Entity import Entity
from code.Shots import Shot


class Player(Entity):
    def __init__(self, name: str, position: tuple, controls: dict, speed: int = 5):
        super().__init__(name, position, path='./asset/Players/')
        self.speed = speed
        self.controls = controls
        self.shot_sprite = SHOT_SPRITES.get(name, "Player1Shot")
        self.shot_direction = 1  # Direção do tiro
        self.shots = []
        self.shoot_cooldown = 300  # Cadência de tiro em milissegundos
        self.last_shot_time = 0
        self.health = ENTITY_HEALTH.get(name , 500)

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
        self.rect.clamp_ip(pygame.Rect(0, 0, WIN_WIDTH, WIN_HEIGHT))

    def shoot(self , current_time):
        """Dispara um tiro se a cadência permitir."""
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.last_shot_time = current_time
            # Cria um tiro partindo do centro direito da nave
            shot = Shot(self.shot_sprite , (self.rect.right , self.rect.centery) , speed=8 , direction=1)
            self.shots.append(shot)
