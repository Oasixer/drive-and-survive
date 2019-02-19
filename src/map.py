import pygame as pg
from locations import Shop
from scene import Scene
from camera import MapCamera
from entity import Entity


class Player(Entity):
    def __init__(self):
        super().__init__()
        self.location = [0, 0]
        self.image = pg.image.load("../include/player_icon_test.png"
                                   ).convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        for action in self.inputs:
            if action in ("up", "left", "down", "right"):
                self.move(action)
            elif action == "pause":
                # TODO: Should be PauseScreen()
                self.manager.go_to(Scene())


class MapData:
    def __init__(self):
        self.locations = []
        vision_radius = 100
        self.camera = MapCamera(vision_radius)
        starter_shop = Shop()
        self.locations = [starter_shop]
        self.player = Player()


class MapScene(Scene):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.player = self.data.map_data.player
        self.locations = self.data.map_data.locations

        self.inputs = []
        self.player.inputs = self.inputs
        self.player.manager = self.data.manager
        self.bg = pg.Surface(
            (self.data.map_data.map_width, self.data.map_data.map_height)
        )
        self.bg.convert()
        self.bg.fill(pg.Color("#0094FF"))
        self.camera = MapCamera

    def update(self):
        for loc in self.locations:
            loc.pos_screen = (loc.pos[0], -self.data.WIN_HEIGHT - loc.pos[1])
        self.player.pos_screen = (self.player.pos[0])
        pass

    def render(self):
        self.data.screen.fill(pg.Color("#0094FF"))
        for loc in self.locations:
            self.data.screen.blit(
                loc.image, self.camera.get_rect_relative_to_screen(loc)
            )
        self.data.screen.blit(
            self.player.image,
            self.camera.get_rect_relative_to_screen(self.player)
        )

    def handle_events(self, events):
        self.inputs = self.data.get_inputs(pg.key.get_pressed())
