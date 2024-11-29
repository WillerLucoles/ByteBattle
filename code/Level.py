import pygame
from code.Const import COLOR_WHITE, WIN_HEIGHT, TIMEOUT_LEVEL
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player
from pygame import Surface, Rect
from pygame.font import Font


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = EntityFactory.get_entity("Fase_1")

        # Inicializar jogadores com base no modo de jogo
        self.player1 = Player("player1", (10, WIN_HEIGHT / 2), controls={
            'up': pygame.K_w,
            'down': pygame.K_s,
            'left': pygame.K_a,
            'right': pygame.K_d
        })

        self.player2 = None  # Somente criado no modo competitivo
        if self.game_mode == "NEW GAME 2P":
            self.player2 = Player("player2", (10, WIN_HEIGHT / 2.6), controls={
                'up': pygame.K_UP,
                'down': pygame.K_DOWN,
                'left': pygame.K_LEFT,
                'right': pygame.K_RIGHT
            })

        # Inicializar inimigos usando a fábrica
        self.enemies = EntityFactory.get_entity("Enemies")

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

            # Atualizar e desenhar todas as entidades
            for ent in self.entity_list:
                ent.move()
                self.window.blit(ent.surf, ent.rect)

            # Atualizar e desenhar Player 1
            self.player1.move()
            self.window.blit(self.player1.surf, self.player1.rect)

            # Atualizar e desenhar Player 2
            if self.player2:
                self.player2.move()
                self.window.blit(self.player2.surf, self.player2.rect)

            # Atualizar e desenhar inimigos
            active_enemies = 0
            for enemy in self.enemies:
                enemy.move()
                if enemy.active:
                    active_enemies += 1
                    self.window.blit(enemy.surf, enemy.rect)

            # Garantir que o número de inimigos ativos não exceda o limite
            if active_enemies < 4:  # Define o número máximo de inimigos ativos
                for enemy in self.enemies:
                    if not enemy.active:
                        enemy.activate()
                        break

            # Exibe informações do nível
            self._render_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self._render_text(14, f'FPS: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self._render_text(14, f'Entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()

            # Processa eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    return "quit"

        return "exit"

    def _render_text(self, size: int, text: str, color: tuple, position: tuple):
        """Renderiza texto na tela."""
        font: Font = pygame.font.SysFont("Lucida Sans Typewriter", size)
        surf: Surface = font.render(text, True, color).convert_alpha()
        rect: Rect = surf.get_rect(left=position[0], top=position[1])
        self.window.blit(surf, rect)
