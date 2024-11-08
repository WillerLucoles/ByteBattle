import pygame
from Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))
        print('Setup start')


    def run(self, ):
        print("Loop Start")
        while True:
            menu = Menu(self.window)

            # Check for all events
           # for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #        pygame.quit()  # close Window
            #        quit()  # end pygame
