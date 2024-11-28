import pygame
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity("Fase_1"))
        print(f"Level initialized: {self.name}, Game mode: {self.game_mode}")
        print(f"Entities loaded: {len(self.entity_list)}")

    def run(self):
        print("Level run started...")  # Verifica se o metodo run está sendo chamado
        running = True
        while running:
            #print("Running level...")  # Diagnóstico para verificar se o loop está rodando
            self.window.fill((0, 0, 0))  # Limpar a tela com preto

            # Atualizar e desenhar todas as entidades
            for ent in self.entity_list:
                ent.move()  # Chama o metodo de movimento
                #print(f"Drawing entity: {ent.name}")  # Diagnóstico para verificar se as entidades estão sendo desenhadas
                self.window.blit(ent.surf, ent.rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Quitting level...")
                    running = False
                    pygame.quit()
                    return "quit"

        print("Exiting level...")
        return "exit"
