from game_states.scene_management.scene import Scene
from utils.camera import LevelCamera


class LevelScene(Scene):
    def __init__(self, data, level_data):
        self.data = data
        self.level_data = level_data
        self.inputs = []
        self.camera = LevelCamera()
        self.screen = self.data.screen
        self.ship = self.data.player.ship
        self.screen_rect = self.data.screen_rect