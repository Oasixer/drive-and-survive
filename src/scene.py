import pygame as pg


class Scene:
    def __init__(self):
        pass

    def render(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError
