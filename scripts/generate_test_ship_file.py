import sys, os

# ok this is a little janky but I couldnt get it to import this shit because its not technically in a package.
# should probably just make this whole game into a package but im too lazy today
# someone remind me to do that <3
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from entities.modules.iron import IronModule
from entities.modules.module_base import ModSize
from entities.vehicles.player_ship import PlayerShip
from utils.load_dump_data import generate_ship_file


def generate(shipNum=0):
    if shipNum == 0:
        modules = [
            IronModule(ModSize.large, (80, 90)),
            IronModule(ModSize.large, (-80, 90)),
            IronModule(ModSize.large, (0, 170)),
            IronModule(ModSize.large, (0, 170 + 80)),
            IronModule(ModSize.large, (0, 170 + 160)),
        ]
        #IronModule(ModSize.small, (0, 140))
        test_ship = PlayerShip(modules)
        generate_ship_file(test_ship)


if __name__ == '__main__':
    generate(0)