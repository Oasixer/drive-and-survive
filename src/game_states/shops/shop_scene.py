import pygame as pg

from game_states.scene_management.scene import Scene
from game_states.shops.toolbar import InventoryToolbar
from game_states.shops.toolbar import ShopToolbar
from utils.camera import ShopCamera


class ShopScene(Scene):
    def __init__(self, data, shop_data):
        super().__init__()
        self.data = data
        self.shop_data = shop_data
        self.inputs = []
        self.camera = ShopCamera()
        self.screen = self.data.screen
        self.ship = self.data.player.ship
        self.screen_rect = self.data.screen_rect
        self.grabbed_mod = None
        self.setup_toolbars()

    def setup_toolbars(self):
        self.toolbars = ["shop", "inv"]
        self.toolbars[0] = ShopToolbar(height=self.screen_rect.height - 120)
        self.toolbars[0].rect.centery = self.screen_rect.centery
        self.toolbars[0].rect.right = self.screen_rect.right
        self.toolbars[1] = InventoryToolbar(height=self.screen_rect.height - 120)
        self.toolbars[1].rect.centery = self.screen_rect.centery
        self.toolbars[1].rect.right = self.toolbars[0].rect.left - 80
        self.toolbars[0].set_contents(self.shop_data.shop_mods)
        self.toolbars[1].set_contents()
        for toolbar in self.toolbars:
            toolbar.scene = self
            toolbar.data = self.data
            toolbar.screen = self.screen
            toolbar.screen_rect = self.screen_rect
            toolbar.update_image()

    def render(self):
        self.ship.render(screen=self.screen)
        for toolbar in self.toolbars:
            self.data.screen.blit(toolbar.image, toolbar.rect)
        if self.grabbed_mod is not None:
            self.camera.blit_rel(self.grabbed_mod)

    def show_scene_info(self):
        super().show_scene_info(extra_messages=[f'Your money$$$$$: {self.data.player.money}'])

    def update(self):
        self.data.screen.fill(pg.Color("GRAY"))
        for toolbar in self.toolbars:
            toolbar.update_image()
            toolbar.check_grabs()

    def handle_events(self, events):
        self.inputs = self.data.get_inputs(pg.key.get_pressed())
        for action in self.inputs:
            if action == "fire":
                self.manager.go_to(self.data.map_scene)
