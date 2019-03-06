from entities.modules.module_base import ModSize
from entities.modules.module_base import Module


class IronModule(Module):
    def __init__(self, size, offset):
        super().__init__(size=size, color="GREY", offset=offset)
        self.cost = self.size.value * self.size.value