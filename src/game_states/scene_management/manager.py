from game_states.menus.title_scene import TitleScene


class SceneManager:
    def __init__(self):
        self.go_to(TitleScene())

    def go_to(self, scene):
        self.scene = scene
