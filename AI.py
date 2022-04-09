import random

from PlayerInterface import Player
from UnitInterface import Unit
from Archer import Archer
from Wizard import Wizard
from Swordsman import Swordsman


class AI(Player):
    def __init__(self, player_name: str):
        self.name = player_name

    def act(self, players: dict):
        enemy_target = self.choose_target_player(players)
        acting_unit = self.choose_acting_unit(players)


    def choose_target_player(self, players: dict):
        # list_of_sorted_players = sorted(players.items(), key=lambda x: x[1])                            #todo smart enemy choose depend on enemy player squad_hp
        # dict_of_sorted_players = dict(list_of_sorted_players)
        enemy_target = random.choice([player for player in players.keys() if player != self])
        return enemy_target

    def choose_acting_unit(self, players: dict):
        acting_unit = random.choice(list(self.squad.keys()))                                            #todo smart unit choose in depend on unit hp, enemies squad hp
        return acting_unit

    def choose_action(self, unit: Unit):
        actions = [unit.attack(), unit.heal()]
        random.choice(actions)                                                                      #todo smart choose of action
