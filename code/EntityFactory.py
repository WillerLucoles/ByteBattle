from code.Background import Background
from code.Const import WIN_WIDTH , WIN_HEIGHT , ENTITY_HEALTH , ENTITY_SPEED
import random

from code.Enemies import Enemy


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str):
        print(f"Creating entity: {entity_name}")

        match entity_name:
            case 'Fase_1':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'City1_Bg{i}', (0, 0)))
                    list_bg.append(Background(f'City1_Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Enemies':
                enemies = []
                for i in range(6):
                    enemy_name = f'Enemy{i + 1}'
                    position = (WIN_WIDTH, random.randint(0, WIN_HEIGHT - 50))
                    speed = ENTITY_SPEED.get(enemy_name, 3)
                    health = ENTITY_HEALTH.get(enemy_name, 20)
                    print(f"Creating enemy {enemy_name} with health {health}")
                    enemies.append(Enemy(enemy_name, position, speed, health))
                return enemies
