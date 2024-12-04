import pygame
from code.Const import COLOR_WHITE , WIN_HEIGHT , TIMEOUT_LEVEL , WIN_WIDTH
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

    def run(self , start_time=1):
        """Loop principal do nível."""
        pygame.mixer_music.load('../asset/Backgrounds/Level/SomLevel1.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)

        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(60)
            self.window.fill((0 , 0 , 0))

            current_time = pygame.time.get_ticks()  # Tempo atual
            elapsed_time = (current_time - start_time) / 1000  # Tempo decorrido em segundos
            remaining_time = max(0 , self.timeout / 1000 - elapsed_time)  # Tempo restante

            # Verifica se o tempo acabou
            if remaining_time <= 0:
                print("[DEBUG] Time's up! Level finished.")
                return "time_over"
            

            # Atualizar e desenhar entidades (Background, etc.)
            for ent in self.entity_list:
                ent.move()
                self.window.blit(ent.surf , ent.rect)

            # Verificar e recriar inimigos se necessário
            EntityMediator.verify_health(self.entity_list , self.enemies)

            # Atualizar e desenhar Player 1
            self.player1.move()
            self.player1.shoot(current_time)  # Player 1 dispara automaticamente
            self.window.blit(self.player1.surf , self.player1.rect)
            for shot in self.player1.shots:
                shot.move()
                self.window.blit(shot.surf , shot.rect)

            # Atualizar e desenhar Player 2
            if self.player2:
                self.player2.move()
                self.player2.shoot(current_time)  # Player 2 dispara automaticamente
                self.window.blit(self.player2.surf , self.player2.rect)
                for shot in self.player2.shots:
                    shot.move()
                    self.window.blit(shot.surf , shot.rect)

            # Atualizar e desenhar inimigos
            for enemy in self.enemies:
                enemy.move()
                enemy.shoot(current_time)  # Enemies disparam automaticamente
                self.window.blit(enemy.surf , enemy.rect)
                for shot in enemy.shots:
                    shot.move()
                    self.window.blit(shot.surf , shot.rect)

            # Verificar colisões entre tiros e entidades
            EntityMediator.check_shot_collisions(self.player1.shots , self.enemies)
            if self.player2:
                EntityMediator.check_shot_collisions(self.player2.shots , self.enemies)
            for enemy in self.enemies:
                EntityMediator.check_shot_collisions(enemy.shots ,
                                                     [self.player1 , self.player2] if self.player2 else [self.player1])

            # Verificar se algum jogador morreu
            if self.player1.health <= 0 or (self.player2 and self.player2.health <= 0):
                print("[DEBUG] Game over due to player health reaching zero!")
                running = False
                break

            # Exibe informações do nível
            self._render_text(14 , f'Player 1 Health: {self.player1.health}' , COLOR_WHITE , (10 , 5))
            if self.player2:
                self._render_text(14 , f'Player 2 Health: {self.player2.health}' , COLOR_WHITE , (10 , 25))
            self._render_text(14 , f'Time Left: {remaining_time:.1f}s' , COLOR_WHITE , (10 , 45))
            self._render_text(14 , f'FPS: {clock.get_fps():.0f}' , COLOR_WHITE , (10 , WIN_HEIGHT - 35))

            pygame.display.flip()

            # Processa eventos
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

    def _render_text(self, size: int, text: str, color: tuple, position: tuple):
        """Renderiza texto na tela."""
        font: Font = pygame.font.SysFont("Lucida Sans Typewriter", size)
        surf: Surface = font.render(text, True, color).convert_alpha()
        rect: Rect = surf.get_rect(left=position[0], top=position[1])
        self.window.blit(surf, rect)

    def pause_menu(self):
        font = pygame.font.SysFont("Lucida Sans Typewriter" , 30)
        options = ["Continue" ,  "Exit"]
        selected = 0

        while True:
            self.window.fill((0 , 0 , 0))
            for i , option in enumerate(options):
                color = (255 , 255 , 255) if i == selected else (100 , 100 , 100)
                text_surf = font.render(option , True , color)
                text_rect = text_surf.get_rect(center=(WIN_WIDTH // 2 , WIN_HEIGHT // 2 + i * 40))
                self.window.blit(text_surf , text_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return "exit"

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = (selected - 1) % len(options)
                    if event.key == pygame.K_DOWN:
                        selected = (selected + 1) % len(options)
                    if event.key == pygame.K_RETURN:
                        return options[selected].lower()
