import pygame as pg


class Camera:
    def __init__():
        raise NotImplementedError

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
    def __init__(self, vision_radius):
        buffer_ = 50
        screen_rect = pg.display.get_surface().get_rect()
        self.camera_rect = pg.Rect(
            screen_rect.centerx - vision_radius - buffer_,
            screen_rect.centery - vision_radius - buffer_,
            (2 * vision_radius + buffer_), (2 * vision_radius + buffer_)
        )

    def get_rect_relative_to_screen(self, target):
        rect = pg.Rect(target)
        rect.centerx = self.camera.centerx - target.pos[0]
        rect.centery = self.camera.centery + target.pos[1]
        return rect