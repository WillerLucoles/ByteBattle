import pygame
from Code.Const  import WIN_WIDTH, WIN_HEIGHT
from Code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        print('Setup start')


    def run(self):
        print("Loop Start")
        while True:
            menu = Menu(self.window)
            menu.run()
            pass


