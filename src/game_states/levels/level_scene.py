import pygame as pg

from game_states.scene_management.scene import Scene
from utils.camera import LevelCamera


class LevelScene(Scene):
    def __init__(self, data, level_data):
        self.data = data
        self.level_data = level_data
        self.ship = self.data.player.ship
        self.ship.make_sprite_group()
        self.object_group = pg.sprite.Group([self.ship.sprite_group, self.level_data.enemy_group])
        self.inputs = []
        self.camera = LevelCamera()
        self.screen = self.data.screen
        self.screen_rect = self.data.screen_rect

    def update(self):
        self.screen.fill(pg.Color("BLACK"))
        pass

    def render(self):
        self.object_group.draw(self.screen)

    def handle_events(self, events):
        pass
