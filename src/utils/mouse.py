import pygame as pg


def get_mouse_interactions(target):
    clicks = pg.mouse.get_pressed()
    hovered = get_hovered(target)
    return (hovered, clicks if hovered else (0, 0, 0))


def get_clicked(target, button=0):
    clicks = pg.mouse.get_pressed()
    return get_hovered(target) and clicks[button]


def get_hovered(target):
    mx, my = pg.mouse.get_pos()
    return (mx > target.left) and (mx < target.right) and (my < target.bottom) and (my > target.top)
