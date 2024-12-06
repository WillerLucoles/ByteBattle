import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_WHITE
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window):
        self.window = window
        self.font_title = pygame.font.SysFont("Lucida Sans Typewriter", 40)
        self.font_text = pygame.font.SysFont("Lucida Sans Typewriter", 20)
        self.db = DBProxy()  # Conexão com o banco de dados

    def run(self):
        """Exibe a tela de score."""
        running = True

        while running:
            self.window.fill((0, 0, 0))  # Fundo preto

            # Título "SCORE"
            title_surf = self.font_title.render("SCORE", True, COLOR_WHITE)
            title_rect = title_surf.get_rect(center=(WIN_WIDTH // 2, 50))
            self.window.blit(title_surf, title_rect)

            # Carregar scores do banco
            scores = self.db.get_scores()  # Retorna uma lista de (player, score, date)
            y_offset = 120

            # Exibir scores
            for player, score, _ in scores:
                player_text = self.font_text.render(f"{player}", True, COLOR_WHITE)
                score_text = self.font_text.render(f"{score}", True, COLOR_WHITE)

                player_rect = player_text.get_rect(left=100, top=y_offset)
                score_rect = score_text.get_rect(right=WIN_WIDTH - 100, top=y_offset)

                self.window.blit(player_text, player_rect)
                self.window.blit(score_text, score_rect)

                y_offset += 30

            pygame.display.flip()

            # Processar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return "quit"

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return "menu"  # Voltar ao menu principal
