# Cores usadas no jogo
from typing import Dict , Any

COLOR_VIVIDSKYBLUE = (85, 205, 241)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_BLACK = (0, 0, 0)
COLOR_GREEN = (0, 128, 0)
COLOR_CYAN = (0, 128, 128)

# Opções do menu principal
MENU_OPTION = ('NEW GAME 1P', 'NEW GAME 2P', 'SCORE', 'EXIT')

# Dimensões da janela do jogo
WIN_WIDTH = 576
WIN_HEIGHT = 354
WIN_CENTER = (WIN_WIDTH // 2, WIN_HEIGHT // 2)

# Fontes padrão
FONT_DEFAULT = "Lucida Sans Typewriter"
FONT_SIZE_LARGE = 20
FONT_SIZE_SMALL = 12

# Sons do jogo
SOUND_MENU = "../asset/Backgrounds/Bg_Menu_Sound.mp3"

#Background do Level1
ENTITY_SPEED = {
    'City1_Bg0': 0,
    'City1_Bg1': 1,
    'City1_Bg2': 2,
    'City1_Bg3': 3,
    'City1_Bg4': 4,
    "Player1": 5,
    "Player2": 5,
    "Enemy1": 2,
    "Enemy2": 3,
    "Enemy3": 1,
    "Enemy4": 2,
    "Enemy5": 2,
    "Enemy6": 3,
}

ENTITY_HEALTH: dict[str | Any, int | Any]={
    'City1_Bg0': 999 ,
    'City1_Bg1': 999 ,
    'City1_Bg2': 999 ,
    'City1_Bg3': 999 ,
    'City1_Bg4': 999 ,
    "Player1": 500 ,
    "Player2": 500 ,
    "Enemy1": 20,
    "Enemy2": 25,
    "Enemy3": 30,
    "Enemy4": 35,
    "Enemy5": 40,
    "Enemy6": 45,

}

# Opcoes de Timed
TIMEOUT_STEP = 100  # 100ms
TIMEOUT_LEVEL = 20000  # 20s