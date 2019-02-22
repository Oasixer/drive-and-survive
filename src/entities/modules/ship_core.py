import pygame as pg

from entities.modules.module_base import ModSize
from entities.modules.module_base import Module
from entities.modules.module_base import RectLocations
from entities.modules.port import Port


class ShipCore(Module):
    def __init__(self, parent_ship):
        super().__init__(
            attached_to=parent_ship, image=pg.image.load("../resources/ship_basic_test.png").convert())
        self.set_both_rects()
        self.ports = [Port(size=ModSize.large, side=RectLocations.bottom, offset=(0, 0), attached_to=self)]

    def set_both_rects(self):
        self.rect.center = (0, 0)
        self.rect_rel = self.rect.copy()
        self.rect_rel.center = self.attached_to.center_rel