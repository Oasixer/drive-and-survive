import pygame as pg

from data.data import GlobalData
from game_states.scene_management.scene import Scene
from utils.load_dump_data import load_ship_file


class LevelScene(Scene):
    def __init__(self):
        self.data = GlobalData()
        self.screen = self.data.screen
        self.ship = load_ship_file()
        self.ship.generate_image_recursive()
        self.ship.generate_rect_recursive()
        self.ship.place_in_scene((self.data.cx, self.data.cy - 300))
        self.ship.add_player()
        self.inputs = []

    def update(self):
        move_directions = [0, 0]
        for input_string in self.inputs:
            if input_string == "up":
                move_directions[1] -= 1
            elif input_string == "down":
                move_directions[1] += 1
            elif input_string == "left":
                move_directions[0] -= 1
            elif input_string == "right":
                move_directions[0] += 1

        if move_directions[0] != 0 or move_directions[1] != 0:
            self.ship.player.move(move_directions)

        # Temp
        #self.ship.update_position_recursive(move_directions)

    def render(self):
        self.screen.fill(pg.Color(self.background_color))
        self.ship.render()

    def handle_events(self, events):
        self.inputs = self.data.get_inputs(pg.key.get_pressed())
        for input_string in self.inputs:
            if input_string == "fire":
                self.ship.player.interact('fire')
        # Doesn't use the inputs until update runs
