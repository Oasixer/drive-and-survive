import pygame as pg
import utils.mouse as mouse

from entities.entity_base import Entity
from entities.modules.module_base import ModSize
from entities.modules.module_base import module_test
from game_states.levels.level_scene import LevelScene
from game_states.shops.shop_scene import ShopScene


class MapIcon(Entity):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.manager = self.data.manager

    def update(self):
        if mouse.get_hovered(self.rect_rel):
            self.data.screen.blit(self.image_on_hover, self.rect_on_hover)
        if mouse.get_clicked(self.rect_rel):
            self.enter()

    def handle_events(self, events):
        raise NotImplementedError


class PlayerMapIcon(Entity):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("../resources/player_icon_test.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)

    def update(self):
        for action in self.inputs:
            if action in ("up", "left", "down", "right"):
                self.move(action)
            elif action == "pause":
                # TODO: Should be PauseScreen()
                #self.manager.go_to(Scene())
                pass


class ShopIcon(MapIcon):
    def __init__(self, data, location, shop_data):
        super().__init__(data)
        self.shop_data = shop_data
        self.grow_amount = 8
        self.icon_size = ModSize.medium
        self.image, self.rect = module_test(self.icon_size, "ORANGE")
        self.image_on_hover = pg.transform.scale(
            self.image.copy(), (self.rect.width + self.grow_amount, self.rect.height + self.grow_amount))
        self.rect_on_hover = self.image_on_hover.get_rect()
        self.rect.center = location
        self.rect_on_hover.center = location

    def update(self):
        super().update()

    def enter(self):
        self.manager.go_to(ShopScene(self.data, self.shop_data))


class LevelIcon(MapIcon):
    def __init__(self, data, location, level_data):
        super().__init__(data)
        self.level_data = level_data
        self.grow_amount = 8
        self.icon_size = ModSize.medium
        self.image, self.rect = module_test(self.icon_size, "BLUE")
        self.image_on_hover = pg.transform.scale(
            self.image.copy(), (self.rect.width + self.grow_amount, self.rect.height + self.grow_amount))
        self.rect_on_hover = self.image_on_hover.get_rect()
        self.rect.center = location
        self.rect_on_hover.center = location

    def update(self):
        super().update()

    def enter(self):
        self.manager.go_to(LevelScene(self.data, self.level_data))
