from entities.modules.module_base import ModSize
from entities.modules.module_base import Module
from entities.modules.module_base import RectLocations
from entities.modules.port import Port


class IronModule(Module):
    def __init__(self, size, side=None, offset=None, attached_to=None):
        super().__init__(size=size, color="GREEN", offset=offset, attached_to=attached_to, side=side)
        self.ports = None
        self.cost = 500

    def init_ports(self):
        self.ports = [
            Port(size=ModSize.large, side=RectLocations.bottom, offset=(0, 0), attached_to=self),
            Port(
                size=ModSize.small,
                side=RectLocations.left,
                offset=(0, self.size.value / 2),
                attached_to=self)
        ]