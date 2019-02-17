import pygame as pg
import os
from world import WorldScene, WorldData
from scene_manager import SceneManager

SCREEN_SIZE = (1600, 900)
CAPTION="FUCK"
pg.font.init()
myfont = pg.font.SysFont('Comic Sans MS', 30)

class Data:
    def __init__(self):
        self.WorldData = WorldData()
        self.WIN_WIDTH = 1600
        self.HALF_WIDTH = self.WIN_WIDTH/2
        self.WIN_HEIGHT = 900
        self.HALF_HEIGHT = self.WIN_HEIGHT/2
        self.SCREEN_SIZE = (self.WIN_WIDTH, self.WIN_HEIGHT)
        self.screen = pg.display.get_surface()
        #other data here

class Game:
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pg.init()
        pg.display.set_caption(CAPTION)
        pg.display.set_mode(SCREEN_SIZE)
        self.fps = 60
        self.clock = pg.time.Clock()
        self.keys = pg.key.get_pressed()
        self.manager = SceneManager()  # This goes to titlescene
        self.manager.scene.data = self.data

    def main_loop(self):
        while(True):
            self.clock.tick(self.fps)/1000.0
            self.handle_events()
            self.manager.scene.update()
            self.manager.scene.render(self.screen)
            pg.display.flip()

    def handle_events(self):
        events = pg.event.get()
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                quit()
        self.manager.scene.handle_events(events)
'''
    def update(self):
        for entity in self.entities:
            entity.update()

    def render(self):
        for sprite in self.sprites:
            sprite.draw()

        pg.display.update()'''

game = Game()
game.main_loop()
