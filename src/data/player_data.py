from entities.vehicles.player_ship import PlayerShip


class PlayerData:
    def __init__(self):
        self.ship = PlayerShip()
        self.money = 1000