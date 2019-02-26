import pygame as pg

from data.data import GlobalData
from entities.entity_base import Entity
from enum import Enum


class ModSize(Enum):
    small = 20
    medium = 40
    large = 80


class RectLocations(Enum):
    center = 1
    top = 2
    bottom = 3
    left = 4
    right = 5


class Module(Entity):
    def __init__(self, size=None, color=None, side=None, offset=None, attached_to=None, image=None):
        super().__init__()
        self.data = GlobalData()
        self.grow_amount = 8  # This has to be an even number because of pixel math
        self.hovered = False
        self.size = size
        self.image = image
        if self.image is None:
            self.image, self.rect = module_test(size, color)
        else:
            self.rect = self.image.get_rect()
        self.image_on_hover = pg.transform.scale(
            self.image.copy(), (self.rect.width + self.grow_amount, self.rect.height + self.grow_amount))
        self.rect_on_hover = self.image_on_hover.get_rect()
        self.offset = offset
        self.attached_to = attached_to
        self.side = side

    def set_both_rects(self, attached_to=None, side=None, offset=None):
        if side is not None:
            self.side = side
        if attached_to is not None:
            self.attached_to = attached_to
        if offset is not None:
            self.offset = offset
        else:
            if side is not None:
                self.side = side
            if attached_to is not None:
                self.attached_to = attached_to
            #print(f"rect bottom of attached {self.attached_to.rect.bottom}")
            #print(f"attached to side {self.side}")
            if offset is not None:
                self.offset = offset
            if self.side == RectLocations.center:
                self.rect.centerx = self.attached_to.rect.centerx + self.offset[0]
                self.rect.centery = self.attached_to.rect.centery - self.offset[1]
            elif self.side == RectLocations.bottom:
                #print(f"offset {self.offset}")
                self.rect.top = self.attached_to.rect.bottom - self.offset[1]
                self.rect.centerx = self.attached_to.rect.centerx + self.offset[0]
                #print(f"top:{self.rect.top}")
            elif self.side == RectLocations.left:
                self.rect.right = self.attached_to.rect.left - self.offset[0]
                self.rect.bottom = self.attached_to.rect.centery + self.offset[1]
        self.offset_center = (self.rect.centerx - self.attached_to.rect.centerx,
                              self.rect.centery - self.attached_to.rect.centery)
        self.set_rect_rel()

    def set_rect_rel(self):
        self.rect_rel = self.rect.copy()
        self.rect_rel.centerx = self.attached_to.rect_rel.centerx + self.offset_center[0]
        self.rect_rel.centery = self.attached_to.rect_rel.centery + self.offset_center[1]

    def blit_from_parent(self):
        self.data.screen.blit(self.image, self.rect_rel)

    def add_attached(self, mod, parent_ship):
        parent_ship.add_module(mod)
        mod.init_ports()

    def replace(self, mod, parent_ship):
        mod.offset = (0, 0)
        mod.side = self.side
        mod.rect = self.rect
        mod.rect_rel = self.rect_rel
        self.attached_to.add_attached(mod, parent_ship)
        self.kill()


def module_test(size, color):
    image = pg.Surface((size.value, size.value))
    image.fill(pg.Color(color))
    return image, image.get_rect()
