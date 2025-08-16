import pygame
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_BROWN, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(80, "Knight", COLOR_BROWN, ((WIN_WIDTH / 2), 50), "./asset/BLKCHCRY.TTF")
            self.menu_text(60, "Jump", COLOR_BROWN, ((WIN_WIDTH / 2), 110), "./asset/BLKCHCRY.TTF" )

            for i in range(len(MENU_OPTION)):
                self.menu_text(30, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 170 + 20 * i), None)

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  pygame.quit()  # Close window
                  quit()  # end pg

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple,
                  font_path: str = "./asset/BLKCHCRY.TTF"):
        text_font = pygame.font.Font(font_path, text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)


#"./asset/BLKCHCRY.TTF"