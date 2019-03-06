import pygame as pg

from data.data import GlobalData
from entities.entity_base import Entity


class Ship(Entity):
    def __init__(self, modules=[]):
        super().__init__()

        self.image_path = "../resources/ship_basic_test.png"
        self.modules = modules  # TEMP, there should be base modules
        #for mod in self.modules:
        #    mod.lock_to(self)
        self.speed = 1

    def generate_image_recursive(self):
        self.data = GlobalData()
        self.screen = self.data.scr
        # Generates or loads an image for itself and all its modules
        self.image = pg.image.load(self.image_path).convert()
        for mod in self.modules:
            mod.generate_color_image()

    def generate_rect_recursive(self):
        self.rect = self.image.get_rect()
        # Note: None of these rects know where they are positioned until you use place_in_scene
        for mod in self.modules:
            mod.generate_rect()

    def place_in_scene(self, pos):
        # Make sure that you set the offsets of the modules before using this
        # Also the pos paramater is absolute, not relative to the center
        # So calculate the screen's center first if you want to place the ship based on that.
        self.rect.center = pos
        for mod in self.modules:
            mod.offset_from_ship(pos)
        #Need more code for when you load a ship with modules on it already

    def update_position_recursive(self, delta):
        self.rect.centerx += delta[0]
        self.rect.centery += delta[1]
        for mod in self.modules:
            mod.rect.centerx += delta[0]
            mod.rect.centery += delta[1]

    def render(self):
        self.screen.blit(self.image, self.rect)
        for mod in self.modules:
            self.screen.blit(mod.image, mod.rect)
