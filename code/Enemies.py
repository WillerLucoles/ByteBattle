from code.Const import WIN_WIDTH , WIN_HEIGHT
from code.Entity import Entity
import random


class Enemy(Entity):
    def __init__(self, name: str, position: tuple, speed: int = 5, health: int = 100):
        super().__init__(name, position, path='../asset/Enemies/')
        self.speed = speed
        self.health = health
        self.active = False
        self.timer = random.randint(30, 150)  # Tempo até reaparecer, em frames
       #print(f"[DEBUG] Enemy created: {name}, Health: {health}, Speed: {speed}")

    def move(self):
        """Move o inimigo horizontalmente e reposiciona se sair da tela."""
        self.rect.x -= self.speed  # Move para a esquerda

        # Reposicionar inimigo
        if self.rect.right < 0:
            self.rect.x = WIN_WIDTH
            self.rect.y = random.randint(0 , WIN_HEIGHT - self.rect.height)  # Novo Y aleatório
            #print(f"[DEBUG] Enemy repositioned: {self.name} (X: {self.rect.x}, Y: {self.rect.y})")



    def activate(self):
        """Ativa o inimigo e define nova posição aleatória."""
        self.active = True
        self.rect.x = 576  # Reaparece à direita da tela
        self.rect.y = random.randint(0, 354 - self.rect.height)  # Novo Y aleatório

    def deactivate(self):
        """Desativa o inimigo e reinicia o timer."""
        self.active = False
        self.timer = random.randint(30, 150)
