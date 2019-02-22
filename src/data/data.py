import pygame as pg

from data.player_data import PlayerData
from enum import Enum
from game_states.map.map_data import MapData


class Keys(Enum):
    # Documentation for keys: https://www.pygame.org/docs/ref/key.html
    w = pg.K_w
    a = pg.K_a
    s = pg.K_s
    d = pg.K_d
    e = pg.K_e
    up_arrow = pg.K_UP
    left_arrow = pg.K_LEFT
    down_arrow = pg.K_DOWN
    right_arrow = pg.K_RIGHT
    space = pg.K_SPACE
    esc = pg.K_ESCAPE
    backspace = pg.K_BACKSPACE
    enter = pg.K_RETURN


class Keybinds(Enum):
    up = Keys.w.value
    down = Keys.s.value
    left = Keys.a.value
    right = Keys.d.value
    enter = Keys.enter.value
    fire = Keys.space.value
    quit = Keys.esc.value


class Data:
    def __init__(self, manager):
        pg.font.init()
        self.font = pg.font.SysFont('Comic Sans MS', 30)
        self.manager = manager
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.HALF_WIDTH = self.screen_rect.height / 2
        self.HALF_HEIGHT = self.screen_rect.height / 2
        self.map_data = MapData(self)
        self.player = PlayerData(self)
        ''' Might not need this:
        self.keybinds = {}
        for bind in Keybinds:
            self.keybinds[bind.name] = bind.value'''

    # TODO: In the future, this function should probably take keybinds as parameters
    # So that you can have diff players with diff keybinds and a single player having different keybinds for different states.
    def get_inputs(self, keys):
        pressed = []
        for keybind in Keybinds:
            if keys[keybind.value]:
                if keybind == Keybinds.quit:
                    pg.quit()
                    quit()
                pressed.append(keybind.name)
        return pressed
