import pygame as pg

import utils

from entity import Entity
from shop_scene import ShopScene


class Location(Entity):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.manager = self.data.manager

    def update(self):
        if utils.get_clicked(self.rect_rel):
            self.enter()

    def handle_events(self, events):
        raise NotImplementedError


class Shop(Location):
    def __init__(self, data, location, shop_data):
        super().__init__(data)
        print("shop init")
        self.shop_data = shop_data
        self.image = pg.Surface((30, 30))
        self.image.fill(pg.Color("RED"))
        self.rect = self.image.get_rect()
        self.rect.center = location

    def update(self):
        super().update()

    def enter(self):
        print("enter")
        self.manager.go_to(ShopScene(self.data, self.shop_data))
