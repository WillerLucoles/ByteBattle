from code.Entity import Entity
import random


class Enemy(Entity):
    def __init__(self, name: str, position: tuple, speed: int = 5):
        super().__init__(name, position, path='../asset/Enemies/')
        self.speed = speed
        self.active = False  # O inimigo começa inativo
        self.timer = random.randint(30, 150)  # Tempo até reaparecer, em frames

    def move(self):
        """Move o inimigo se estiver ativo."""
        if not self.active:
            self.timer -= 1
            if self.timer <= 0:
                self.activate()
            return

        self.rect.x -= self.speed

        # Reposicionar inimigo se sair completamente pela esquerda
        if self.rect.right < 0:
            self.deactivate()

    def activate(self):
        """Ativa o inimigo e define nova posição aleatória."""
        self.active = True
        self.rect.x = 576  # Reaparece à direita da tela
        self.rect.y = random.randint(0, 354 - self.rect.height)  # Novo Y aleatório

    def deactivate(self):
        """Desativa o inimigo e reinicia o timer."""
        self.active = False
        self.timer = random.randint(30, 150)  # Define novo tempo de espera
