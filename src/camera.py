import pygame as pg

class Camera:
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pg.Rect(0, 0, width, height)

    def apply(self, target):
        try:
            return target.rect.move(self.state.topleft)
        except AttributeError:
            return map(sum, zip(target, self.state.topleft))

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)