import pygame as pg

from data.data import GlobalData
from entities.modules.module_base import Module
from entities.vehicles.ship_base import Ship


class PlayerShip(Ship):
    def __init__(self, modules=[]):
        super().__init__(modules)
        self.data = GlobalData()

    def add_player(self):
        self.player = PlayerTest(self)

    def render(self):
        super().render()
        self.data.scr.blit(self.player.image, self.player.rect)


class PlayerTest:
    def __init__(self, ship):
        self.ship = ship
        self.image_path = '../resources/player.png'
        self.image = pg.image.load(self.image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.cabin.rect.centerx
        self.rect.bottom = ship.cabin.rect.bottom
        ship.cabin.player = self
        self.speed = 4
        self.using_console = False

    def move(self, direct):
        if self.using_console:
            self.ship.update_position_recursive(direct)
            self.rect.centerx += direct[0] * self.ship.speed
            self.rect.centery += direct[1] * self.ship.speed
        else:
            self.move_player_inside(direct)

    def move_player_inside(self, direct):
        new_left = self.rect.left + direct[0] * self.speed
        new_right = self.rect.right + direct[0] * self.speed
        if new_left < self.ship.cabin.rect.left:
            self.rect.left = self.ship.cabin.rect.left
        elif new_right > self.ship.cabin.rect.right:
            self.rect.right = self.ship.cabin.rect.right
        else:
            self.rect.left = new_left

    def interact(self, action):
        if action == 'fire':
            if self.using_console == False:
                self.using_console = self.ship.cabin.get_console_interactions()
            else:
                self.using_console = False

        # Nah ur stuck on the floor no going up
        #self.rect.centery += direct[1]
