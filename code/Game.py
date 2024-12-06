import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Menu import Menu
from code.Level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Byte Battle")
        self.clock = pygame.time.Clock()

    def start_new_game(self):
        running = True
        while running:
            self.window.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return "quit"
            pygame.display.flip()
            self.clock.tick(60)

    def run(self):
        while True:
            print("Entering menu...")
            menu = Menu(self.window)
            menu_return = menu.run()
            print(f"Menu option selected: {menu_return}")

            if menu_return in ["NEW GAME 1P", "NEW GAME 2P"]:
                print("Initializing level...")

                try:
                    level = Level(self.window, "Level 1", menu_return)
                    print(f"Level initialized: {level}")
                except Exception as e:
                    print(f"Error initializing level: {e}")
                    continue

                level_return = level.run()

                if level_return == "quit":
                    break

                if level_return == "menu":
                    print("Returning to main menu...")
                    continue

            elif menu_return == "EXIT":
                pygame.quit()
                break

if __name__ == "__main__":
    try:
        game = Game()
        game.run()
    except Exception as e:
        print(f"Unexpected error: {e}")
        pygame.quit()
