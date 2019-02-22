from entities.modules.module_base import Module
from entities.modules.ship_core import ShipCore
from entities.vehicles.ship_base import Ship


class PlayerShip(Ship):
    def __init__(self, screen, type=0):
        super().__init__(screen)
        self.center_rel = self.screen_rect.center
        self.base = ShipCore(self)
        self.modules = [self.base]
