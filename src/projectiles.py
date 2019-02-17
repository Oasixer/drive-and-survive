import pygame as pg


class Projectile(pg.sprite.Sprite):
    def __init__(self, position, velocity, sprite, movement="normal", duration=None):
        pass


class Bomb(Projectile):
    def __init__(self, position, velocity):
        sprite = None
        Projectile.__init__(position, velocity, sprite)
        pass


class Bullet(Projectile):
    def __init__(self, position, velocity):
        sprite = None
        Projectile.__init__(position, velocity, sprite)


class Laser(Projectile):
    def __init__(self, position, velocity):
        sprite = None
        Projectile.__init__(position, velocity, sprite)