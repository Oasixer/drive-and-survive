import pygame as pg

import utils.mouse as mouse

from entities.entity_base import Entity
from entities.modules.module_base import ModSize
from entities.modules.port import Port


class Toolbar(Entity):
    def __init__(self, width, height):
        super().__init__()
        self.set_contents()
        toolbar_width = width
        toolbar_height = height
        self.image = pg.Surface((toolbar_width, toolbar_height))
        self.image.fill(pg.Color("RED"))
        self.rect = self.image.get_rect()

    def check_grabs(self):
        for modlist in self.mods.values():
            for mod in modlist:
                mod.hovered = mouse.get_hovered(mod.rect_rel)
                if mod.hovered:
                    self.scene.ship.render(self.screen, render_single_type=Port, port_size=mod.size)
                    if self.scene.grabbed_mod is not None:
                        if pg.mouse.get_pressed()[0]:
                            self.scene.grabbed_mod = mod
                        else:
                            self.scene.grabbed_mod = None
                            self.drop_mod(mod)
                    else:
                        #TODO: Update line below
                        if type(self) is ShopToolbar:
                            textsurface = self.data.font.render(
                                f'This is a FUCKING GREEN AS SHIT module. Cost is ${mod.cost}', False,
                                (0, 0, 0))
                        else:
                            textsurface = self.data.font.render(f'You already FUCKING BOUGHT this BRO.....',
                                                                False, (0, 0, 0))
                        self.screen.blit(textsurface, (500, 30))
                        if pg.mouse.get_pressed()[0]:
                            self.scene.grabbed_mod = mod
                        else:
                            self.scene.grabbed_mod = None

    def set_contents(self, mods=[]):
        self.mods = {size: [mod for mod in mods if mod.size == size] for size in ModSize}

    def add_contents(self, mod=None):
        self.mods[mod.size].append(mod)
        #print(f"{type(self)} {self.mods}")

    def update_image(self):
        #TODO: Only update when the user buys a mod or hovers or stops hovering or on INIT
        spacing_base = 15
        spacing_total = spacing_base
        self.image.fill(pg.Color("RED"))
        for size, modlist in self.mods.items():
            for mod in modlist:
                rect = mod.rect_on_hover if mod.hovered else mod.rect
                rect_rel = pg.Rect(
                    rect)  # Test out of curiosity if changing this can change reference vs copy object
                rect_rel.centerx = self.rect.centerx
                rect.centerx = self.rect.width / 2
                rect.bottom = size.value + spacing_total
                rect_rel.bottom = self.rect.top + size.value + spacing_total
                mod.rect_rel = rect_rel
                if mod is self.scene.grabbed_mod:
                    mod.rect_rel.center = pg.mouse.get_pos()
                    #self.screen.blit(mod.image, mod.rect_rel)
                else:
                    self.image.blit(mod.image_on_hover if mod.hovered else mod.image,
                                    rect.move(0, mod.grow_amount / 2) if mod.hovered else rect)
                spacing_total += size.value + spacing_base


class InventoryToolbar(Toolbar):
    def __init__(self, height, width=160):
        super().__init__(width, height)

    def drop_mod(self, mod):
        for module in self.scene.ship.modules:
            if module.ports is not None:
                for port in module.ports:
                    if mouse.get_hovered(port.rect_rel):
                        port.replace(
                            mod=self.mods[mod.size].pop(self.mods[mod.size].index(mod)),
                            parent_ship=self.data.player.ship)


class ShopToolbar(Toolbar):
    def __init__(self, height, width=160):
        super().__init__(width, height)

    def drop_mod(self, mod):
        for toolbar in self.scene.toolbars:
            if toolbar is not self:
                if mouse.get_hovered(toolbar.rect):
                    self.data.player.money -= mod.cost
                    toolbar.add_contents(self.mods[mod.size].pop(self.mods[mod.size].index(mod)))
                    return

        for module in self.scene.ship.modules:
            if module.ports is not None:
                for port in module.ports:
                    if mouse.get_hovered(port.rect_rel):
                        port.replace(
                            mod=self.mods[mod.size].pop(self.mods[mod.size].index(mod)),
                            parent_ship=self.data.player.ship)
                    self.data.player.money -= mod.cost
                    return