from entities.modules.iron import IronModule
from entities.modules.module_base import ModSize
from game_states.levels.level_data import LevelData
from game_states.map.icons import LevelIcon
from game_states.map.icons import PlayerMapIcon


class MapData:
    def __init__(self):
        first_level_enemies = []
        first_level_data = LevelData(first_level_enemies)
        first_level_icon = LevelIcon((-100, 250), first_level_data)
        self.locations = [first_level_icon]
        self.player_map_icon = PlayerMapIcon((0, 0))