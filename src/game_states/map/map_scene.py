import pygame as pg

from data.data import GlobalData
from game_states.scene_management.scene import Scene
from utils.camera import MapCamera


class MapScene(Scene):
    def __init__(self):
        super().__init__()
        self.data = GlobalData()
        self.screen = self.data.screen
        self.data.map_scene = self
        self.map_data = self.data.map_data
        self.camera = MapCamera()
        self.player_map_icon = self.map_data.player_map_icon
        self.locations = self.map_data.locations
        self.inputs = []
        self.player_map_icon.inputs = self.inputs
        self.camera.set_rect_rel(self.player_map_icon)
        for loc in self.locations:
            self.camera.set_rect_rel(loc)
            loc.rect_on_hover.center = loc.rect_rel.center
            print(loc.rect_rel)
        # Super temporary
        self.bg_map_area = pg.display.get_surface()
        self.bg_map_area.convert()
        self.bg_map_area.fill(pg.Color("#0094FF"))

    def update(self):
        self.data.screen.fill(pg.Color("#0094FF"))
        for loc in self.locations:
            loc.update()

    def render(self):
        for loc in self.locations:
            self.camera.blit_rel(loc)
            #print(self.camera.get_rect_relative_to_screen(loc))

        self.camera.blit_rel(self.player_map_icon)

    def handle_events(self, events):
        self.inputs = self.data.get_inputs(pg.key.get_pressed())
