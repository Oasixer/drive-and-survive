import pygame as pg

from vehicles import PlayerShip


class PlayerData:
    def __init__(self, data):
        self.data = data
        self.ship = PlayerShip(self.data.screen)
        self.money = 1000