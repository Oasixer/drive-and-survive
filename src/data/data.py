import pygame as pg

from enum import Enum


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


class GlobalData:
    def __new__(cls):

        if not hasattr(cls, 'instance'):

            cls.instance = super(GlobalData, cls).__new__(cls)

        return cls.instance

    def get_inputs(self, keys):
        pressed = []
        for keybind in Keybinds:
            if keys[keybind.value]:
                if keybind == Keybinds.quit:
                    pg.quit()
                    quit()
                pressed.append(keybind.name)
        return pressed


'''class GlobalData:
    val = {}

    def __init__(self, val):
        self.val = val

    def __getitem__(self, key):
        return self.val[key]

    def __setitem__(self, key, val):
        self.val[key] = val

    @classmethod
    def get(cls):
        return cls.__init__(cls.val)'''