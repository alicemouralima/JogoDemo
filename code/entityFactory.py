#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH
from code.background import Background
#from code.plataforma import Plataforma


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

    #def create_plataformas(self):
     #   plataformas = []

      #  plataformas.append(Plataforma(100, 400, 3))
       # plataformas.append(Plataforma(300, 300, 7))
        #plataformas.append(Plataforma(50, 200, 15))

        #return plataformas

