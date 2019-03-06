from data.data import GlobalData
from entities.modules.module_base import Module
from entities.vehicles.ship_base import Ship


class PlayerShip(Ship):
    def __init__(self, modules=[]):
        super().__init__(modules)
        self.data = GlobalData()
