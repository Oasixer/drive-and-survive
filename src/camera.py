import pygame as pg


class Camera:
    def __init__(self):
        self.screen = pg.display.get_surface()

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
    def __init__(self):
        super().__init__()
        self.screen_rect = self.screen.get_rect()

    def set_rect_rel(self, target):
        rect = target.rect
        rect.centerx = self.screen_rect.centerx + target.rect.centerx
        rect.centery = self.screen_rect.centery - target.rect.centery
        target.rect_rel = rect

    def update_rect_rel(self, target, offset):
        pass

    def blit_rel(self, target):
        self.screen.blit(target.image, target.rect_rel)


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
