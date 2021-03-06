import pygame as pg

from data.data import GlobalData
from game_states.scene_management.scene import Scene

#from utils.camera import MapCamera


class MapScene(Scene):
    def __init__(self):
        super().__init__()
        self.data = GlobalData()
        self.screen = self.data.screen
        self.data.map_scene = self
        self.map_data = self.data.map_data
        self.player_map_icon = self.map_data.player_map_icon
        self.locations = self.map_data.locations
        self.inputs = []
        self.player_map_icon.inputs = self.inputs
        self.entities = [self.player_map_icon] + self.locations
        for entity in self.entities:
            entity.rect.center = (self.data.cx + entity.pos_from_center[0],
                                  self.data.cy - entity.pos_from_center[1])
        self.screen.fill(pg.Color("#0094FF"))

    def update(self):
        for loc in self.locations:
            loc.update()

    def render(self):
        self.data.screen.fill(pg.Color("#0094FF"))  #TODO: shouldnt need to fill screen until render time
        for entity in self.entities:
            self.screen.blit(entity.image, entity.rect)

    def handle_events(self, events):
        self.inputs = self.data.get_inputs(pg.key.get_pressed())
