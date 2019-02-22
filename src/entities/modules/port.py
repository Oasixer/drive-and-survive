from entities.modules.module_base import Module


class Port(Module):
    def __init__(self, size, offset, attached_to, side):
        super().__init__(size=size, color="YELLOW", offset=offset, attached_to=attached_to, side=side)
        self.set_both_rects()