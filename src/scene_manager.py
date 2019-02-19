from menu import TitleScene


class SceneManager:
    def __init__(self):
        self.go_to(TitleScene())

    def go_to(self, scene):
        self.scene = scene
        print("Set")
        self.scene.manager = self