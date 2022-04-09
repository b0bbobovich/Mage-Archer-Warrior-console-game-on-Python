import abc
from UnitInterface import Unit
from Archer import Archer
from Wizard import Wizard
from Swordsman import Swordsman

class Player:
    @abc.abstractmethod
    def __init__(self, player_name: str):
        self.squad = {}
        archer: Unit = Archer()
        wizard: Unit = Wizard()
        swordsman: Unit = Swordsman()
        self.squad[archer] = archer.unit_params
        self.squad[wizard] = wizard.unit_params
        self.squad[swordsman] = swordsman.unit_params
        self.squad_hp = archer.unit_params['HP'] + wizard.unit_params['HP'] + swordsman.unit_params['HP']



