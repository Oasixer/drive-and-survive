from entities.vehicles.player_ship import PlayerShip


class PlayerData:
    def __init__(self, data):
        self.data = data
        self.ship = PlayerShip(self.data.screen)
        # TODO: This shouldn't really need the screen here - the ship should have some secondary initialization
        # that can be done when it actually gets used
        self.money = 1000