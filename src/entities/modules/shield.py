import pygame as pg

from entities.modules.module_base import ModSize
from entities.modules.module_base import Module


class ShieldModule(Module):
    def __init__(self, size, offset):
        super().__init__(size=size, offset=offset)
        self.cost = self.size.value * self.size.value

    def generate_image(self):
        self.image_path = '../resources/shield_medium.png'
        if self.size == ModSize.medium:
            self.image = pg.image.load(self.image_path).convert()