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
            print(f"Menu option selected: {menu_return}")  # Verifica qual opção foi escolhida

            if menu_return in ["NEW GAME 1P" , "NEW GAME 2P"]:  # "NEW GAME 1P" ou "NEW GAME 2P"
                print("Initializing level...")

                try:
                    level = Level(self.window , "Level 1" , menu_return)  # Nova instância do level
                    print(f"Level initialized: {level}")
                except Exception as e:
                    print(f"Error initializing level: {e}")
                    continue  # Retorna ao menu caso ocorra erro ao inicializar o level

                level_return = level.run()  # Executa o nível

                if level_return == "quit":  # Se o jogador quiser sair
                    break

                if level_return == "menu":  # Se o jogador terminar o level e voltar ao menu
                    print("Returning to main menu...")
                    continue  # Reinicia o loop, levando o jogador de volta ao menu inicial

            elif menu_return == "EXIT":  # Caso o jogador selecione EXIT
                pygame.quit()
                break

if __name__ == "__main__":
    try:
        game = Game()
        game.run()
    except Exception as e:
        print(f"Unexpected error: {e}")
        pygame.quit()
