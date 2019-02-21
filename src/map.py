import pygame as pg

from camera import MapCamera
from entity import Entity
from locations import Shop
from modules import IronModule
from modules import ModSize
from scene import Scene
from shop_scene import ShopData


class PlayerMapIcon(Entity):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("../include/player_icon_test.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)

    def update(self):
        for action in self.inputs:
            if action in ("up", "left", "down", "right"):
                self.move(action)
            elif action == "pause":
                # TODO: Should be PauseScreen()
                self.manager.go_to(Scene())


class MapData:
    def __init__(self, data):
        self.data = data
        self.locations = []
        first_shop_modules = [IronModule(ModSize.small), IronModule(ModSize.large)]
        first_shop = Shop(self.data, (300, 300), ShopData(mods=first_shop_modules))
        self.locations = [first_shop]
        self.player_map_icon = PlayerMapIcon()


class MapScene(Scene):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.map_data = self.data.map_data
        self.camera = MapCamera()
        self.player_map_icon = self.map_data.player_map_icon
        self.locations = self.data.map_data.locations
        self.inputs = []
        self.player_map_icon.inputs = self.inputs
        self.player_map_icon.manager = self.data.manager
        self.camera.set_rect_rel(self.player_map_icon)
        for loc in self.locations:
            self.camera.set_rect_rel(loc)
            print(loc.rect_rel)
        # Super temporary
        self.bg_map_area = pg.display.get_surface()
        self.bg_map_area.convert()
        self.bg_map_area.fill(pg.Color("#0094FF"))

    def update(self):
        for loc in self.locations:
            loc.update()

    def render(self):
        self.data.screen.fill(pg.Color("#0094FF"))
        for loc in self.locations:
            self.camera.blit_rel(loc)
            #print(self.camera.get_rect_relative_to_screen(loc))
        self.camera.blit_rel(self.player_map_icon)

    def handle_events(self, events):
        self.inputs = self.data.get_inputs(pg.key.get_pressed())
