from entities.modules.iron import IronModule
from entities.modules.module_base import ModSize
from game_states.levels.level_1 import LevelOne
from game_states.map.icons import LevelIcon
from game_states.map.icons import PlayerMapIcon


class MapData:
    def __init__(self):
        first_level_icon = LevelIcon((-100, 250), LevelOne)
        self.locations = [first_level_icon]
        self.player_map_icon = PlayerMapIcon((0, 0))