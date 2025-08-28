# C
import pygame
from pygame.examples.grid import WINDOW_WIDTH

C_PURPLE = (138, 43, 226)
C_LAVENDER = (200, 162, 200)
C_ORANGE = (255, 140, 0)
C_GREEN = (0, 128, 0)
C_CIANO = (0, 128, 128)
C_WHITE = (255, 255, 255)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level2Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy2': 60
}
ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level2Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 25,
    'Enemy1': 5,
    'Enemy2': 6
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level2Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy2': 125
}
ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15
}
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level2Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Player1': 4,
    'Player1Shot': 2,
    'Player2': 4,
    'Player2Shot': 2,
    'Enemy1': 2,
    'Enemy2': 1
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_SPACE,
                    'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 1000

# T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 30000
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
SCORE_POS = {'Title':(WINDOW_WIDTH / 2 - 110, 50),
             'EnterName':(WINDOW_WIDTH / 2 - 110, 80),
             'Label':(WINDOW_WIDTH / 2 - 110, 90),
             'Name':(WINDOW_WIDTH / 2 - 110, 110),
             0:(WINDOW_WIDTH / 2 - 110, 110),
             1:(WINDOW_WIDTH / 2 - 110, 130),
             2:(WINDOW_WIDTH / 2 - 110, 150),
             3:(WINDOW_WIDTH / 2 - 110, 170),
             4:(WINDOW_WIDTH / 2 - 110, 190),
             5:(WINDOW_WIDTH / 2 - 110, 210),
             6:(WINDOW_WIDTH / 2 - 110, 230),
             7:(WINDOW_WIDTH / 2 - 110, 250),
             8:(WINDOW_WIDTH / 2 - 110, 270),
             9:(WINDOW_WIDTH / 2 - 110, 290)
}
