import os
import pygame as pg

from data.data import GlobalData
from game_states.scene_management.manager import SceneManager

CAPTION = "FUCK"
SCREEN_SIZE = (1400, 855)


class Game:
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pg.init()
        pg.display.set_caption(CAPTION)
        pg.display.set_mode(SCREEN_SIZE)
        self.fps = 60
        self.clock = pg.time.Clock()
        self.keys = pg.key.get_pressed()
        data = GlobalData()
        pg.font.init()
        data.font = pg.font.SysFont('Comic Sans MS', 30)
        data.scr = pg.display.get_surface()
        data.screen = data.scr
        data.rect = data.scr.get_rect()
        data.screen_rect = data.rect
        data.cy = data.rect.centery
        data.cx = data.rect.centerx
        data.c = data.rect.center
        data.t = data.rect.top
        data.b = data.rect.bottom
        data.l = data.rect.left
        data.r = data.rect.right
        data.manager = SceneManager()
        self.manager = data.manager

    def main_loop(self):
        while (True):
            self.clock.tick(self.fps) / 1000.0
            self.handle_events()
            self.manager.scene.update()
            self.manager.scene.render()
            self.manager.scene.show_scene_info()
            pg.display.flip()

    def handle_events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type in [pg.KEYUP, pg.KEYDOWN]:
                self.manager.scene.handle_events(events)


game = Game()
game.main_loop()
