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
SOUND_MENU = "./asset/Backgrounds/Bg_Menu_Sound.mp3"

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
    "Player1": 600 ,
    "Player2": 600 ,
    "Enemy1": 10,
    "Enemy2": 20,
    "Enemy3": 10,
    "Enemy4": 20,
    "Enemy5":30,
    "Enemy6": 20,

}

SHOT_SPRITES = {
    "Player1": "Player1Shot",
    "Player2": "Player2Shot",
    "Enemy": "EnemyShot"
}

# Pontuações de inimigos
entity_Score = {
    "Enemy1": 100,
    "Enemy2": 200,
    "Enemy3": 150,
    "Enemy4": 250,
    "Enemy5": 300,
    "Enemy6": 400
}

# Opcoes de Timed
TIMEOUT_STEP = 100  # 100ms
TIMEOUT_LEVEL = 10000  # 20s