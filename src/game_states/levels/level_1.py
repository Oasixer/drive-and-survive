import pygame as pg

from game_states.levels.level_scene import LevelScene


class LevelOne(LevelScene):
    def __init__(self):
        super().__init__()
        self.enemies = []
        self.background_color = 'BLUE'
        self.scene_messages = [
            'Walk over to the ship controls console and press space to drive!',
            'Press space again to stop using.'
        ]

    def render(self):
        super().render()

    def update(self):
        super().update()

    def handle_events(self, events):
        super().handle_events(events)

    def show_scene_info(self):
        super().show_scene_info(extra_messages=self.scene_messages)