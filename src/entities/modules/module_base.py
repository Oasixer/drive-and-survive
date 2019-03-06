import pygame as pg

from data.data import GlobalData
from entities.entity_base import Entity
from enum import Enum


class ModSize(Enum):
    small = 20
    medium = 40
    large = 80


class Module(Entity):
    def __init__(self, size, color=None, offset=None):
        super().__init__()
        self.data = GlobalData()
        self.color = color
        self.size = size
        self.offset = offset  # Default offset from the center of the ship

    def generate_color_image(self):
        color = self.color
        self.image = module_test(self.size, color)

    def load_image(self):
        # This is for when modules actually have art
        # Hashtag KAT WHERE U AT
        # I couldn't just use a hashtag because all the comments start with hash already
        # Kill me now
        raise NotImplementedError

    def generate_rect(self):
        self.rect = self.image.get_rect()

    def offset_from_ship(self, ship_center):
        self.rect.centerx = ship_center[0] + self.offset[0]
        self.rect.centery = ship_center[1] + self.offset[1]

    '''def lock_to(self, locked_to):
        self.locked_to = locked_to
        self.offset = (self.rect.centerx - locked_to.rect.centerx, self.rect.centery - locked_to.rect.centery)'''
    '''def update_position(self):
        self.rect.centerx = self.locked_to.centerx + self.offset[0]
        self.rect.centery = self.locked_to.centery + self.offset[1]'''


def module_test(size, color):
    image = pg.Surface((size.value, size.value))
    image.fill(pg.Color(color))
    return image
