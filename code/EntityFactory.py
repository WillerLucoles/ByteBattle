from code.Player import Player
from code.Background import Background
from code.Const import WIN_WIDTH , WIN_HEIGHT


class EntityFactory:

    get = None

    @staticmethod
    def get_entity(entity_name: str):
        print(f"Creating entity: {entity_name}")  # Verifica se o nome da entidade é o esperado
        match entity_name:
            case 'Fase_1':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'City1_Bg{i}', (0, 0)))
                    list_bg.append(Background(f'City1_Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1' , (10, WIN_HEIGHT / 2))

