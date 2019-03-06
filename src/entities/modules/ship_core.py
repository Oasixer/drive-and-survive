import pygame as pg

from entities.modules.module_base import ModSize
from entities.modules.module_base import Module
from entities.modules.port import Port


class ShipCore(Module):
    def __init__(self, ship):
        super().__init__(ModSize.large)
        self.offset = (0, 0)
        self.ship = ship