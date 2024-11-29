import pygame
from code.Const import COLOR_WHITE, WIN_HEIGHT, TIMEOUT_LEVEL
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from pygame import Surface, Rect
from pygame.font import Font


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = EntityFactory.get_entity("Fase_1")
        # Testes
        # print(f"Level initialized: {self.name}, Game mode: {self.game_mode}")
        # print(f"Entities loaded: {len(self.entity_list)}")

    def run(self):
        """Loop principal do nível."""
        pygame.mixer_music.load('../asset/Backgrounds/Level/SomLevel1.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)

        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(60)
            self.window.fill((0, 0, 0))  # Limpa a tela a cada iteração

            # Atualiza e desenha todas as entidades
            for ent in self.entity_list:
                ent.move()
                self.window.blit(ent.surf, ent.rect)

            # Exibe informações do nível
            self._render_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self._render_text(14, f'FPS: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self._render_text(14, f'Entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()  # Atualiza a tela

            # Processa eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # teste
                    # print("Quitting level...")
                    running = False
                    pygame.quit()
                    return "quit"

        # teste
        # print("Exiting level...")
        return "exit"

    def _render_text(self, size: int, text: str, color: tuple, position: tuple):
        """Renderiza texto na tela."""
        font: Font = pygame.font.SysFont("Lucida Sans Typewriter", size)
        surf: Surface = font.render(text, True, color).convert_alpha()
        rect: Rect = surf.get_rect(left=position[0], top=position[1])
        self.window.blit(surf, rect)
