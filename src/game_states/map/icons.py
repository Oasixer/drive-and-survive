import pygame as pg
import utils.mouse as mouse

from data.data import GlobalData
from entities.entity_base import Entity
from entities.modules.module_base import ModSize
from game_states.levels.level_scene import LevelScene


class MapIcon(Entity):
    def __init__(self, pos_from_center):
        super().__init__()
        self.data = GlobalData()
        self.pos_from_center = pos_from_center

    def update(self):
        if mouse.get_hovered(self.rect):
            self.image = self.image_on_hover
        else:
            self.image = self.image_normal
        if mouse.get_clicked(self.rect):
            self.enter()

    def handle_events(self, events):
        raise NotImplementedError

    def add_hover(self):
        self.image_on_hover = pg.transform.scale(
            self.image_normal.copy(),
            (self.rect.width + self.grow_amount, self.rect.height + self.grow_amount))


class PlayerMapIcon(Entity):
    def __init__(self, pos_from_center):
        super().__init__()
        self.pos_from_center = pos_from_center
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


class LevelIcon(MapIcon):
    def __init__(self, pos_from_center, level_data):
        super().__init__(pos_from_center)
        self.level_data = level_data
        self.grow_amount = 8
        self.icon_size = ModSize.medium
        self.image_normal, self.rect = temporary_icon_generator(self.icon_size, "BLUE")
        self.add_hover()

    def update(self):
        super().update()

    def enter(self):
        self.data.manager.go_to(LevelScene(self.level_data))


def temporary_icon_generator(size, color):
    image = pg.Surface((size.value, size.value))
    image.fill(pg.Color(color))
    return image, image.get_rect()