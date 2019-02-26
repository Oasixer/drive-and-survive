import pygame as pg

from data.data import GlobalData


class testThing(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()


class LevelData:
    def __init__(self, enemies):
        self.data = GlobalData()
        for enemy in enemies:
            enemy.make_sprite_group()
        self.enemy_group = pg.sprite.Group(enemy.sprite_group for enemy in enemies)