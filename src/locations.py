import pygame as pg
from entity import Entity


class Location(Entity):
    def __init__(self):
        super().__init__()

    def update(self):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError


class Shop(Location):
    def __init__(self):
        super().__init__()
        print("shop init")
        self.image = pg.Surface((30, 30))
        self.image.fill(pg.Color("RED"))
        self.pos = (60, 60)
        self.rect = self.image.get_rect()