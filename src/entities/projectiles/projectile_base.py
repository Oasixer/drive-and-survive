from entities.entity_base import Entity


class Projectile(Entity):
    def __init__(self, position, velocity, sprite, movement="normal", duration=None):
        pass


'''
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
        Projectile.__init__(position, velocity, sprite)'''