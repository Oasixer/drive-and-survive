import pygame as pg
import utils.mouse as mouse

from data.data import GlobalData
from entities.entity_base import Entity
from entities.modules.module_base import ModSize
from entities.modules.module_base import module_test
from game_states.levels.level_scene import LevelScene
from game_states.shops.shop_scene import ShopScene


class MapIcon(Entity):
    def __init__(self, pos_from_center):
        super().__init__()
        self.data = GlobalData()
        self.pos_from_center = pos_from_center

    def update(self):
        if mouse.get_hovered(self.rect_rel):
            self.data.screen.blit(self.image_on_hover, self.rect_on_hover)
        if mouse.get_clicked(self.rect_rel):
            self.enter()

    def handle_events(self, events):
        raise NotImplementedError

    def add_hover(self):
        self.image_on_hover = pg.transform.scale(
            self.image.copy(), (self.rect.width + self.grow_amount, self.rect.height + self.grow_amount))
        self.rect_on_hover = self.image_on_hover.get_rect()
        self.rect_on_hover.center = self.rect.center


class PlayerMapIcon(Entity):
    def __init__(self, pos_from_center):
        super().__init__(pos_from_center)
        self.image = pg.image.load("../resources/player_icon_test.png").convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        for action in self.inputs:
            if action in ("up", "left", "down", "right"):
                self.move(action)
            elif action == "pause":
                # TODO: Should be PauseScreen()
                #self.manager.go_to(Scene())
                pass


class ShopIcon(MapIcon):
    def __init__(self, pos_from_center, shop_data):
        super().__init__(pos_from_center)
        self.shop_data = shop_data
        self.grow_amount = 8
        self.icon_size = ModSize.medium
        self.image, self.rect = module_test(self.icon_size, "ORANGE")
        self.add_hover()

    def update(self):
        super().update()

    def enter(self):
        self.data.manager.go_to(ShopScene(self.shop_data))


class LevelIcon(MapIcon):
    def __init__(self, pos_from_center, level_data):
        super().__init__(pos_from_center)
        self.level_data = level_data
        self.grow_amount = 8
        self.icon_size = ModSize.medium
        self.image, self.rect = module_test(self.icon_size, "BLUE")
        self.add_hover()

    def update(self):
        super().update()

    def enter(self):
        self.data.manager.go_to(LevelScene(self.level_data))
