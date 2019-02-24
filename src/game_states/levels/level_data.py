import pygame as pg


class testThing(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()


class LevelData:
    def __init__(self, data, enemies):
        self.data = data
        self.screen = self.data.screen
        self.screen_rect = self.data.screen_rect
        for enemy in enemies:
            enemy.make_sprite_group()
        self.enemy_group = pg.sprite.Group(enemy.sprite_group for enemy in enemies)