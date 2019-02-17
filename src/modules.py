import pygame as pg

class Module(pg.sprite.Sprite):
    def __init__(self, position):
        pass


class EngineModule(Module):
    def __init__(self, model):
        x = None
        y = None
        Module.__init__(x, y)
        #self.sprite = sprite_list[model]