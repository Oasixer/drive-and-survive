import pygame as pg

from data.data import GlobalData
from game_states.scene_management.scene import Scene
from utils.load_dump_data import load_ship_file


class LevelScene(Scene):
    def __init__(self, level_data):
        self.data = GlobalData()
        self.screen = self.data.screen
        self.ship = load_ship_file()
        self.ship.generate_image_recursive()
        self.ship.generate_rect_recursive()
        self.ship.place_in_scene((self.data.cx, self.data.cy - 300))
        self.inputs = []

    def update(self):
        #loop thru inputs and move shit
        pass

    def render(self):
        self.screen.fill(pg.Color("BLACK"))
        self.ship.render()

    def handle_events(self, events):
        self.inputs = self.data.get_inputs(pg.key.get_pressed())
