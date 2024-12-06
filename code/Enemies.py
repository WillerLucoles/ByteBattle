from code.Const import WIN_WIDTH , WIN_HEIGHT , SHOT_SPRITES , ENTITY_HEALTH
from code.Entity import Entity
import random

from code.Shots import Shot


class Enemy(Entity):
    def __init__(self, name: str, position: tuple, speed: int = 5, health: int = 100):
        super().__init__(name, position, path='./asset/Enemies/')
        self.speed = speed
        self.health = ENTITY_HEALTH.get(name, 50)
        self.active = False
        self.timer = random.randint(30, 150)
        self.shot_sprite = SHOT_SPRITES.get("Enemy", "EnemyShot")
        self.shots = []
        self.shoot_cooldown = random.randint(2000, 2500)
        self.last_shot_time = 0

       #print(f"[DEBUG] Enemy created: {name}, Health: {health}, Speed: {speed}")

    def move(self):
        """Move o inimigo horizontalmente e reposiciona se sair da tela."""
        self.rect.x -= self.speed

        # Reposicionar inimigo
        if self.rect.right < 0:
            self.rect.x = WIN_WIDTH
            self.rect.y = random.randint(0 , WIN_HEIGHT - self.rect.height)
            #print(f"[DEBUG] Enemy repositioned: {self.name} (X: {self.rect.x}, Y: {self.rect.y})")



    def activate(self):
        """Ativa o inimigo e define nova posição aleatória."""
        self.active = True
        self.rect.x = 576
        self.rect.y = random.randint(0, 354 - self.rect.height)

    def deactivate(self):
        """Desativa o inimigo e reinicia o timer."""
        self.active = False
        self.timer = random.randint(30, 150)

    def shoot(self , current_time):
        """Dispara um tiro se a cadência permitir."""
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.last_shot_time = current_time

            shot = Shot(self.shot_sprite , (self.rect.left , self.rect.centery) , speed=6 , direction=-1)
            self.shots.append(shot)