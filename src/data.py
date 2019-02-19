import pygame as pg
from enum import Enum
from map import MapData


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
    pause = Keys.esc.value


class Data:
    def __init__(self):
        self.WIN_WIDTH = 1600
        self.HALF_WIDTH = self.WIN_WIDTH / 2
        self.WIN_HEIGHT = 900
        self.HALF_HEIGHT = self.WIN_HEIGHT / 2
        self.SCREEN_SIZE = (self.WIN_WIDTH, self.WIN_HEIGHT)
        self.screen = pg.display.get_surface()
        self.map_data = MapData()
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
                pressed.append(keybind.name)
        return pressed
