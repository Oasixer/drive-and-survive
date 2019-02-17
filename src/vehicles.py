import pygame as pg

class Tank():
    def __init__(self, type):
        self.modules = None  # TEMP, there should be base modules
        self.speed = 1
        self.type = None  # Player, enemy, etc

    def draw(self, screen):
        raise NotImplementedError
        #screen.blit(self.image, self.rect)

class PlayerTank(Tank):
    def __init__(self):
        Tank.__init__(type)
        self.distance_travelled = 0


class EnemyTank(Tank):
    def __init__(self, position, type):
        Tank.__init__(type)
        self.position = position
