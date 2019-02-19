import pygame as pg
from scene import Scene
from data import Data
from map import MapScene, MapData


class TitleScene(Scene):
    def __init__(self):
        super().__init__()
        self.font = pg.font.SysFont('Arial', 56)
        self.sfont = pg.font.SysFont('Arial', 32)
        self.data = Data()
        # This should really be coming from some sort of gui where the player can load old saves and shit

    def render(self):
        # beware: ugly!
        self.data.screen.fill((0, 200, 0))
        text1 = self.font.render('Drive and Survive', True, (255, 255, 255))
        text2 = self.sfont.render('> press space to start <', True,
                                  (255, 255, 255))
        self.data.screen.blit(text1, (200, 50))
        self.data.screen.blit(text2, (200, 350))

    def update(self):
        pass

    def handle_events(self, events):
        print("handling")
        for e in events:
            if e.type == pg.KEYDOWN and e.key == pg.K_SPACE:
                self.data.manager = self.manager
                map_scene = MapScene(self.data)
                self.manager.go_to(map_scene)