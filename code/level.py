#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame import Surface, Rect
from pygame.examples.go_over_there import screen
from pygame.font import Font

from code.Const import WIN_HEIGHT, COLOR_WHITE
from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window=None, name="Default Level", game_mode="Arcade"):
        self.window = window or pygame.display.set_mode((576, 324))
        self.name = name
        self.game_mode = game_mode
        self.entity_list = []
        self.all_sprites = pygame.sprite.Group()

        entities = EntityFactory.get_entity("Level1Bg")
        self.entity_list.extend(entities)
        self.all_sprites.add(entities)

        entities = EntityFactory.get_entity("Level1Platforms")
        self.entity_list.extend(entities)
        self.all_sprites.add(entities)

        entities = EntityFactory.get_entity("Knight_01__IDLE_001")
        self.entity_list.extend(entities)
        self.all_sprites.add(entities)

        self.timeout = 20000

    def update(self):
        self.all_sprites.update()

    def draw(self, surface):
        self.all_sprites.draw(surface)

    def run(self):
        pygame.mixer_music.load(f'./asset/Level1_music.wav')
        pygame.mixer_music.play(-1) #Knight_01__IDLE_001
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.update()
            self.draw(self.window)

            # 📝 HUD
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

