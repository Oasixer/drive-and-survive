import pygame as pg

from entities.entity_base import Entity
from entities.modules.ship_core import ShipCore


class Ship(Entity):
    def __init__(self, screen, type=0):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.modules = None  # TEMP, there should be base modules
        self.speed = 1

    def add_module(self, mod):
        self.modules.append(mod)

    def make_sprite_group(self):
        self.sprite_group = pg.sprite.Group(module for module in self.modules)

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


# TODO: Temp, this isnt being used yet
class EnemyShip(Ship):
    def __init__(self, screen, type=0):
        super().__init__(screen)
        self.center_rel = self.screen_rect.center
        self.base = ShipCore(self)
        self.modules = [self.base]
