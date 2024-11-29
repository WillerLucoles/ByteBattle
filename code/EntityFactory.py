from code.Player import Player
from code.Background import Background
from code.Enemies import Enemy
from code.Const import WIN_WIDTH, WIN_HEIGHT
import random


class EntityFactory:
    get = None

    @staticmethod
    def get_entity(entity_name: str):
        print(f"Creating entity: {entity_name}")  # Diagnóstico de criação

        match entity_name:
            case 'Fase_1':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'City1_Bg{i}', (0, 0)))
                    list_bg.append(Background(f'City1_Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2))

            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2))

            case 'Enemies':
                enemies = []
                for i in range(6):
                    enemy_name = f'enemy{i + 1}'
                    position = (WIN_WIDTH, random.randint(0, WIN_HEIGHT - 50))
                    speed = random.randint(2, 4)
                    enemies.append(Enemy(enemy_name, position, speed))
                return enemies
