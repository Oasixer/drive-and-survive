import pygame as pg

from entity import Entity
from modules import ModSize
from modules import Module
from modules import Port
from modules import RectLocations


class Ship(Entity):
    def __init__(self, screen, type=0):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.modules = None  # TEMP, there should be base modules
        self.speed = 1

    def add_module(self, mod):
        self.modules.append(mod)

    #def set_rect_rel_recursive(self, camera):
    #for module in modules:
    #camera.set_rect_rel(module):

    def render(self, screen, port_size=None, render_single_type=None):
        for module in self.modules:
            if (render_single_type is None) or (type(module) == render_single_type):
                screen.blit(module.image, module.rect_rel)
            if port_size is not None:
                if module.ports is not None:
                    for port in module.ports:
                        if port.size == port_size:
                            port.blit_from_parent(screen)


class BaseShip(Module):
    def __init__(self, parent_ship):
        super().__init__(
            attached_to=parent_ship, image=pg.image.load("../include/ship_basic_test.png").convert())
        self.set_both_rects()
        self.ports = [Port(size=ModSize.large, side=RectLocations.bottom, offset=(0, 0), attached_to=self)]

    def set_both_rects(self):
        self.rect.center = (0, 0)
        self.rect_rel = self.rect.copy()
        self.rect_rel.center = self.attached_to.center_rel


class PlayerShip(Ship):
    def __init__(self, screen, type=0):
        super().__init__(screen)
        self.center_rel = self.screen_rect.center
        self.base = BaseShip(self)
        self.modules = [self.base]
