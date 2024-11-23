import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_WIDTH, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW, WIN_HEIGHT


class Menu:
    """
    This class handles the menu system.
    """
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('../asset/Backgrounds/Bg_Menu.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.logo_surf = pygame.image.load('../asset/Backgrounds/Logo_Menu.png').convert_alpha()

        # Resize the logo
        self.logo_surf = pygame.transform.scale(self.logo_surf,
                                                (self.logo_surf.get_width() // 5, self.logo_surf.get_height() // 5))

        # Center the logo horizontally and position it 30px from the top
        self.logo_rect = self.logo_surf.get_rect(center=(WIN_WIDTH / 2, self.logo_surf.get_height() / 2 + 30))

    def run(self):
        """
        Main loop for the menu, handles rendering and input.
        """
        menuOption = 0
        pygame.mixer_music.load('../asset/Backgrounds/Bg_Menu_Sound.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.drawMenu(menuOption)
            menuOption, selectedOption = self.handleEvents(menuOption)
            if selectedOption:
                return selectedOption

    def drawMenu(self, menuOption):
        """
        Draw the menu options on the screen.
        """
        self.window.blit(source=self.surf, dest=self.rect)

        # Draw the logo instead of "Byte Battle" text
        self.window.blit(source=self.logo_surf, dest=self.logo_rect)

        for i, option in enumerate(MENU_OPTION):
            if i == menuOption:
                # Draw a black transparent rectangle
                rectSurf = pygame.Surface((200, 25), pygame.SRCALPHA)
                rectSurf.fill((0, 0, 0, 128))  # Black with 50% transparency
                rectRect = rectSurf.get_rect(center=((WIN_WIDTH / 2), 200 + 25 * i))
                self.window.blit(rectSurf, rectRect)

                # Draw the text in yellow
                self.menuText(20, option, COLOR_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
            else:
                self.menuText(20, option, COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))
        pygame.display.flip()

    def handleEvents(self, menuOption):
        """
        Handle user input events.
        """
        mousePos = pygame.mouse.get_pos()
        selectedOption = None

        for i, option in enumerate(MENU_OPTION):
            textRect = self.getTextRect(20, option, ((WIN_WIDTH / 2), 200 + 25 * i))
            if textRect.collidepoint(mousePos):
                menuOption = i
                if pygame.mouse.get_pressed()[0]:
                    selectedOption = MENU_OPTION[menuOption]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    menuOption = (menuOption + 1) % len(MENU_OPTION)
                if event.key == pygame.K_UP:
                    menuOption = (menuOption - 1) % len(MENU_OPTION)
                if event.key == pygame.K_RETURN:
                    selectedOption = MENU_OPTION[menuOption]

        return menuOption, selectedOption

    def getTextRect(self, textSize: int, text: str, textCenterPos: tuple) -> Rect:
        """
        Get the rect for the text.
        """
        textFont: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=textSize)
        textSurf: Surface = textFont.render(text, True, COLOR_WHITE).convert_alpha()
        textRect: Rect = textSurf.get_rect(center=textCenterPos)
        return textRect

    def menuText(self, textSize: int, text: str, textColor: tuple, textCenterPos: tuple):
        """
        Render text on the menu.
        """
        textFont: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=textSize)
        textSurf: Surface = textFont.render(text, True, textColor).convert_alpha()
        textRect: Rect = textSurf.get_rect(center=textCenterPos)
        self.window.blit(source=textSurf, dest=textRect)
        return textRect
