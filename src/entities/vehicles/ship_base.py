import pygame as pg

from data.data import GlobalData
from entities.entity_base import Entity
from entities.modules.ship_core import ShipCore


class Ship(Entity):
    def __init__(self, type=0):
        super().__init__()
        self.data = GlobalData()
        self.screen = self.data.scr
        self.rect = self.data.rect
        self.modules = None  # TEMP, there should be base modules
        self.speed = 1

    def add_module(self, mod):
        self.modules.append(mod)

    def make_sprite_group(self):
        self.sprite_group = pg.sprite.Group(module for module in self.modules)

    #def set_rect_rel_recursive(self, camera):
    #for module in modules:
    #camera.set_rect_rel(module):

    def render(self, port_size=None, render_single_type=None):
        for module in self.modules:
            if (render_single_type is None) or (type(module) == render_single_type):
                self.screen.blit(module.image, module.rect_rel)
            if port_size is not None:
                if module.ports is not None:
                    for port in module.ports:
                        if port.size == port_size:
                            port.blit_from_parent()

    def create_image(self, port_size=None, render_single_type=None):
        for module in self.modules:
            spaced_mod = mod.rect_on_hover if mod.hovered = mod.rect
            #if hovering, perform spacing on module and blit to screen
            self.screen.blit(module.image, module.rect_rel)

    def update_image(self, port_size=None, render_single_type=None):
        #call above function to create image of module, then add to port
            for port in module.ports:
                if port.size == port_size:
                    port.blit_from_parent()


# TODO: Temp, this isnt being used yet
class EnemyShip(Ship):
    def __init__(self, type=0):
        super().__init__()
        self.center_rel = self.data.screen_rect.center
        self.base = ShipCore(self)
        self.modules = [self.base]
