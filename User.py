from PlayerInterface import Player
from UnitInterface import Unit
from Archer import Archer
from Wizard import Wizard
from Swordsman import Swordsman

class User(Player):
    def __init__(self, player_name: str):
        self.name = player_name

