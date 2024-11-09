import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from Code.Const import WIN_WIDTH , COLOR_VIVIDSKYBLUE , MENU_OPTION , COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/Backgrounds/Bg_Menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./assets/Backgrounds/Bg_Menu_Sound.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menuText(text_size=50, text="Byte", text_color=COLOR_VIVIDSKYBLUE,
                          text_center_pos=((WIN_WIDTH / 2), 70))
            self.menuText(text_size=50, text="Battle", text_color=COLOR_VIVIDSKYBLUE,
                          text_center_pos=((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menuText(text_size=20 , text=MENU_OPTION[i] , text_color=COLOR_WHITE ,
                              text_center_pos=((WIN_WIDTH / 2) , 200 + 25 * i))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close Window
                    quit()  # end pygame

    def menuText(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucid Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)