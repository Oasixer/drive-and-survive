class Scene:
    def __init__(self):
        pass

    def render(self):
        raise NotImplementedError

    def show_scene_info(self, offset_increment=30, extra_messages=[]):
        font = self.data.font
        screen = self.data.screen
        all_messages = [f"Scene: {type(self)}"] + [message for message in extra_messages]
        offset = 0
        for message in all_messages:
            textsurface = font.render(message, False, (0, 0, 0))
            screen.blit(textsurface, (0, offset))
            offset += offset_increment

    def update(self):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError
