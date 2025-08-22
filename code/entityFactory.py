#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.background import Background
from code.plataforma import Plataforma
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(name=f'Level1Bg{i}', position=(0, 0)))
                    list_bg.append(Background(name=f'Level1Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg

            case 'Player1':
                return [Player(name='Player1', position=(10, WIN_HEIGHT / 2))]

            case 'Level1Platforms':
                list_plataformas = []
                plataformas_data = [
                    {"x": 100, "y": 400, "length": 3, "tile": "./asset/Tile_01.png"},
                    {"x": 300, "y": 350, "length": 5, "tile": "./asset/Tile_02.png"},
                    {"x": 500, "y": 300, "length": 4, "tile": "./asset/Tile_03.png"},
                ]
                for p in plataformas_data:
                    list_plataformas.append(
                        Plataforma(p["x"], p["y"], p["length"], p["tile"])
                    )
                return list_plataformas

            case _:
                return []


