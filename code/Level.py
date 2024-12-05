import pygame
from code.Const import COLOR_WHITE , WIN_HEIGHT , TIMEOUT_LEVEL , WIN_WIDTH , entity_Score , COLOR_VIVIDSKYBLUE , \
    COLOR_YELLOW
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player
from pygame import Surface, Rect
from pygame.font import Font
from code.EntityMediator import EntityMediator


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
        self.player1_score = 0  # Inicializar score do Player 1

        self.player2 = None  # Somente criado no modo competitivo
        self.player2_score = 0  # Inicializar score do Player 2
        if self.game_mode == "NEW GAME 2P":
            self.player2 = Player("player2", (10, WIN_HEIGHT / 2.6), controls={
                'up': pygame.K_UP,
                'down': pygame.K_DOWN,
                'left': pygame.K_LEFT,
                'right': pygame.K_RIGHT
            })

        # Inicializar inimigos usando a fábrica
        self.enemies = EntityFactory.get_entity("Enemies")

    def update_score(self, player, target):
        """Atualiza o score do jogador ao destruir um inimigo."""
        normalized_name = target.name.capitalize()
        points = entity_Score.get(normalized_name, 0)
        if player == "player1":
            self.player1_score += points
        elif player == "player2":
            self.player2_score += points

    def run(self, start_time=1):
        """Loop principal do nível."""
        pygame.mixer_music.load('../asset/Backgrounds/Level/SomLevel1.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)

        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(60)
            self.window.fill((0, 0, 0))  # Limpa a tela

            current_time = pygame.time.get_ticks()
            elapsed_time = (current_time - start_time) / 1000
            remaining_time = max(0, self.timeout / 1000 - elapsed_time)

            if remaining_time <= 0:
                return "time_over"

            for ent in self.entity_list:
                ent.move()
                self.window.blit(ent.surf, ent.rect)

            EntityMediator.verify_health(self.entity_list, self.enemies)

            self.player1.move()
            self.player1.shoot(current_time)
            self.window.blit(self.player1.surf, self.player1.rect)
            for shot in self.player1.shots:
                shot.move()
                for enemy in self.enemies:
                    if shot.rect.colliderect(enemy.rect):
                        self.update_score("player1", enemy)
                        enemy.health = 0
                        if shot in self.player1.shots:
                            self.player1.shots.remove(shot)
                self.window.blit(shot.surf, shot.rect)

            if self.player2:
                self.player2.move()
                self.player2.shoot(current_time)
                self.window.blit(self.player2.surf, self.player2.rect)
                for shot in self.player2.shots:
                    shot.move()
                    for enemy in self.enemies:
                        if shot.rect.colliderect(enemy.rect):
                            self.update_score("player2", enemy)
                            enemy.health = 0
                            if shot in self.player2.shots:
                                self.player2.shots.remove(shot)
                    self.window.blit(shot.surf, shot.rect)

            for enemy in self.enemies:
                enemy.move()
                enemy.shoot(current_time)
                self.window.blit(enemy.surf, enemy.rect)
                for shot in enemy.shots:
                    shot.move()
                    self.window.blit(shot.surf, shot.rect)

            # Exibir informações do nível e jogadores
            self._render_text(16, f"Level 1 - Timeout: {remaining_time:.1f}s", COLOR_WHITE, (10, 10))
            self._render_text(16, f"Player 1 - Health: {self.player1.health} | Score: {self.player1_score}",
                              COLOR_VIVIDSKYBLUE, (10, 25))
            if self.player2:
                self._render_text(16, f"Player 2 - Health: {self.player2.health} | Score: {self.player2_score}",
                                  COLOR_YELLOW, (10, 40))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    return "quit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        result = self.pause_menu()
                        if result == "continue":
                            continue
                        elif result == "cancel":
                            return "menu"
                        elif result == "exit":
                            return "quit"

        return "exit"

    def _render_text(self , size: int , text: str , color: tuple , position: tuple):
        """Renderiza texto na tela com validação de posição."""
        # Verificar se as coordenadas estão dentro dos limites da tela
        if position[0] < 0 or position[1] < 0 or position[0] > WIN_WIDTH or position[1] > WIN_HEIGHT:
            print(f"[ERROR] Invalid position for text: {position}")
            return

        font: Font = pygame.font.SysFont("Lucida Sans Typewriter" , size)
        text_surf: Surface = font.render(text , True , color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=position[0] , top=position[1])
        self.window.blit(text_surf , text_rect)