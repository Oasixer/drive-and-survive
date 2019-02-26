from data.data import GlobalData
from entities.modules.module_base import Module
from entities.modules.ship_core import ShipCore
from entities.vehicles.ship_base import Ship


class PlayerShip(Ship):
    def __init__(self, type=0):
        super().__init__()
        self.data = GlobalData()
        self.center_rel = self.data.c
        self.base = ShipCore(self)
        self.modules = [self.base]
