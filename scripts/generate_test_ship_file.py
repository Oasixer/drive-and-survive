import sys, os

# ok this is a little janky but I couldnt get it to import this shit because its not technically in a package.
# should probably just make this whole game into a package but im too lazy today
# someone remind me to do that <3
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from entities.modules.cabin import CabinModule
from entities.modules.iron import IronModule
from entities.modules.module_base import ModSize
from entities.modules.shield import ShieldModule
from entities.vehicles.player_ship import PlayerShip
from utils.load_dump_data import generate_ship_file


def generate(shipNum=0):
    if shipNum == 0:
        modules = [
            CabinModule((87, 177)),
            ShieldModule(ModSize.medium, (187, 177)),
        ]
        #IronModule(ModSize.small, (0, 140))
        test_ship = PlayerShip(modules)
        test_ship.cabin = modules[0]  # Temp
        generate_ship_file(test_ship)


if __name__ == '__main__':
    generate(0)