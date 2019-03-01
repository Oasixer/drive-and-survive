from entities.modules.iron import IronModule
from entities.modules.module_base import ModSize
from entities.vehicles.ship_base import EnemyShip
from game_states.levels.level_data import LevelData
from game_states.map.icons import LevelIcon
from game_states.map.icons import PlayerMapIcon
from game_states.map.icons import ShopIcon
from game_states.shops.shop_data import ShopData


class MapData:
    def __init__(self):
        first_shop_modules = [
            IronModule(ModSize.small),
            IronModule(ModSize.large)
        ]
        first_shop_icon = ShopIcon(
            (300, 300), ShopData(mods=first_shop_modules)
        )

        first_level_enemies = [EnemyShip()]
        first_level_data = LevelData(first_level_enemies)
        first_level_icon = LevelIcon((-100, 250), first_level_data)
        self.locations = [first_shop_icon, first_level_icon]
        self.player_map_icon = PlayerMapIcon((0, 0))