import pygame as pg

from entities.modules.module_base import ModSize
from entities.modules.module_base import Module


class CabinModule(Module):
    def __init__(self, offset):
        super().__init__(size=None, offset=offset)
        self.player = None
        #self.cost = self.size.value * self.size.value

    def generate_image(self):
        self.image_path = '../resources/cabin.png'
        self.image = pg.image.load(self.image_path).convert()

    def generate_rect(self):
        super().generate_rect()
        self.console_img = pg.Surface((15, 15))
        self.console_img.fill(pg.Color("GRAY"))
        self.console_rect = self.console_img.get_rect()

    def offset_from_ship(self, pos):
        super().offset_from_ship(pos)
        self.console_rect.bottom = self.rect.bottom - 30
        self.console_rect.left = self.rect.left

    def get_console_interactions(self):
        if self.player is not None:
            px = self.player.rect.centerx
            cx = self.console_rect.centerx
            if abs(cx - px) < 30:
                print("detected!")
                return True

    def update_position(self, delta):
        super().update_position(delta)
        self.console_rect.centerx += delta[0]
        self.console_rect.centery += delta[1]
