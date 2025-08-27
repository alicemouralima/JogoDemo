#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from code.level import Level
from code.MenuBg import Menu


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        pygame.mixer_music.load('./asset/Menu.ogg')
        pygame.mixer_music.play(-1)
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)

            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pass

