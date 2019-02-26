import pygame as pg

from data.data import GlobalData
from game_states.scene_management.scene import Scene
from utils.camera import LevelCamera


class LevelScene(Scene):
    def __init__(self, level_data):
        self.data = GlobalData()
        self.screen = self.data.screen
        self.level_data = level_data
        self.ship = self.data.player.ship
        self.ship.make_sprite_group()
        start_pos = (self.data.rect.centery, )
        #self.ship.move_abs(start_pos)
        self.inputs = []
        self.camera = LevelCamera()
        self.screen_rect = self.data.screen_rect

    def update(self):
        self.screen.fill(pg.Color("BLACK"))
        pass

    def render(self):
        #self.object_group.draw(self.screen)
        pass

    def handle_events(self, events):
        pass
