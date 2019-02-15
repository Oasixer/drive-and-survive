import pygame as pg

# TODO: Make a game.


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


class Module(pg.sprite.Sprite):
    def __init__(self, position):
        pass


class EngineModule(Module):
    def __init__(self, model):
        x = None
        y = None
        Module.__init__(x, y)
        #self.sprite = sprite_list[model]


class Tank():
    def __init__(self, type):
        self.modules = None  # TEMP, there should be base modules
        self.speed = 1
        self.type = None  # Player, enemy, etc


class PlayerTank(Tank):
    def __init__(self):
        Tank.__init__(type)
        self.distance_travelled = 0


class EnemyTank(Tank):
    def __init__(self, position, type):
        Tank.__init__(type)
        self.position = position
