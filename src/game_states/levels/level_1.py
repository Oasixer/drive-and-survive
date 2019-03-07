import pygame as pg

from game_states.levels.level_scene import LevelScene


class LevelOne(LevelScene):
    def __init__(self):
        super().__init__()
        self.enemies = []
        self.background_color = 'BLUE'

    def render(self):
        super().render()

    def update(self):
        super().update()

    def handle_events(self, events):
        super().handle_events(events)