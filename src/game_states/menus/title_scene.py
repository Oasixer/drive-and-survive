import pygame as pg

from data.data import GlobalData
from game_states.map.map_data import MapData
from game_states.map.map_scene import MapScene
from game_states.scene_management.scene import Scene


class TitleScene(Scene):
    def __init__(self):
        super().__init__()
        self.font = pg.font.SysFont('Arial', 56)
        self.sfont = pg.font.SysFont('Arial', 32)
        self.data = GlobalData()
        # This should really be coming from some sort of gui where the player can load old saves and shit

    def render(self):
        # beware: ugly!
        self.data.screen.fill((0, 200, 0))
        text1 = self.font.render('Drive and Survive', True, (255, 255, 255))
        text2 = self.sfont.render('> press space to start <', True, (255, 255, 255))
        self.data.screen.blit(text1, (200, 50))
        self.data.screen.blit(text2, (200, 350))

    def update(self):
        pass

    def handle_events(self, events):
        for e in events:
            if e.type == pg.KEYDOWN and e.key == pg.K_SPACE:
                self.data.map_data = MapData()
                map_scene = MapScene()
                self.data.manager.go_to(map_scene)