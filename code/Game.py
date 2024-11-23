import pygame
from code.Const import WIN_WIDTH , WIN_HEIGHT , MENU_OPTION
from code.Menu import Menu
from code.Level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH , WIN_HEIGHT))
        pygame.display.set_caption("Byte Battle")

    def start_new_game(self):
        """
        Start the logic for a new game.
        """
        running = True
        while running:
            self.window.fill((0 , 0 , 0))  # Placeholder for game screen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return "quit"
            pygame.display.flip()

    def run(self):
        print("Loop Start")
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0] , MENU_OPTION[1] , MENU_OPTION[2]]:  # Option for New Game
                # Call the start of the new game, which starts the logic
                game_status = self.start_new_game()
                if game_status == "quit":
                    break

                # Initialize Level 1
                level = Level(self.window , "Level 1" , menu_return)
                level_return = level.run()

                if level_return == "quit":
                    break
                elif level_return == "next":  # Just as an example for level progression
                    pass  # Handle progression to next level if needed

            elif menu_return == MENU_OPTION[4]:  # Quit option
                pygame.quit()
                break


if __name__ == "__main__":
    game = Game()
    game.run()
