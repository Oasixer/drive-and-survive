import pygame as pg

from data.data import GlobalData


class Camera:
    def __init__(self):
        self.data = GlobalData()
        self.screen = self.data.scr
        self.screen_rect = self.data.rect

    def apply(self, target):
        '''try:
            return target.rect.move(self.state.topleft)
        except AttributeError:
            return map(sum, zip(target, self.state.topleft))'''
        #target.rect.centery = self.data.WIN_HEIGHT - target.rect.centery
        raise NotImplementedError

    def update(self, target):
        raise NotImplementedError


class MapCamera(Camera):
    def __init__(self, scene):
        super().__init__()
        self.scene = scene
        for entity in self.scene.entities:
            #print(type(entity))
            entity.rect.center = (
                self.screen_rect.centerx + entity.pos_from_center[0],
                self.screen_rect.centery - entity.pos_from_center[1]
            )
            #print(entity.rect)
        for loc in self.scene.locations:
            loc.add_hover()

    def render_scene(self):
        for entity in self.scene.entities:
            self.screen.blit(entity.image, entity.rect)


class ShopCamera(Camera):
    def __init__(self):
        super().__init__()
        self.screen_rect = pg.display.get_surface().get_rect()

    def set_rect_rel(self, target):
        rect = target.rect
        rect.centerx = self.screen_rect.centerx + target.rect.centerx
        rect.centery = self.screen_rect.centery - target.rect.centery
        target.rect_rel = rect

    def update_rect_rel(self, target, offset):
        pass

    def blit_rel(self, target):
        self.screen.blit(target.image, target.rect_rel)


class LevelCamera(Camera):
    def __init__(self):
        super().__init__()
        self.screen_rect = pg.display.get_surface().get_rect()

    def set_rect_rel(self, target):
        rect = target.rect
        rect.centerx = self.screen_rect.centerx + target.rect.centerx
        rect.centery = self.screen_rect.centery - target.rect.centery
        target.rect_rel = rect

    def update_rect_rel(self, target, offset):
        pass

    def blit_rel(self, target):
        self.screen.blit(target.image, target.rect_rel)
