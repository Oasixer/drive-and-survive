import pygame as pg
from enum import Enum
from shop import Shop
from scene import Scene
from camera import Camera


class LocationTypes(Enum):
    shop = 0
    other_location_example = 1

class WorldData:
    def __init__(self):
        self.locations = []
        self.player_loc = (0,0)
        self.map_width=100
        self.map_height=100
        starter_shop = Shop()
        self.locations = {LocationTypes.shop: [starter_shop]}
        pass #put stuff here

class WorldScene(Scene):
    def __init__(self, world_data):
        super().__init__()
        # This code should be in render?
        self.bg = pg.Surface((32,32)) # Temp BG
        self.bg.convert()
        self.bg.fill(pg.Color("#0094FF")) 

        def complex_camera(camera, target_rect):
            l, t, _, _ = target_rect
            _, _, w, h = camera
            l, t, _, _ = -l + self.data.HALF_WIDTH, -t +self.data.HALF_HEIGHT, w, h

            l = min(0, l)                           # stop scrolling left
            l = max(-(camera.width - self.data.WIN_WIDTH), l)   # stop scrolling right
            t = max(-(camera.height-self.data.WIN_HEIGHT), t) # stop scrolling bottom

            return pg.Rect(l, t, w, h)
        self.camera = Camera(complex_camera, world_data.map_width, world_data.map_height)
   
    def update(self):
        pass

    def render(self):
        pass

