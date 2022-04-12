import abc
from queue import Queue
from bcolors import bcolors
from Archer import Archer
from Wizard import Wizard
from Swordsman import Swordsman


class Player:
    def __init__(self, player_name: str):
        self.player_data = {
            'player': self,
            'player_name': player_name,
            'squad_hp': 0,
            'units': []
        }
        self.units_moves_queue = Queue()

    @abc.abstractmethod
    def form_squad(self):
        pass

    def create_unit(self, unit_type):
        if unit_type == 'archer':
            unit = Archer()
        elif unit_type == 'wizard':
            unit = Wizard()
        else:
            unit = Swordsman()
        self.units_moves_queue.put(unit)
        return unit

    @abc.abstractmethod
    def make_move(self, players: list) -> dict:
        pass

    @abc.abstractmethod
    def attack(self, players: list) -> tuple:
        pass

    @abc.abstractmethod
    def heal(self) -> tuple:
        pass

    def get_alive_unit(self):
        units = []
        for unit_data in self.player_data["units"]:
            units.append(unit_data['unit_obj'])
        active_unit = None
        while not active_unit:
            if not self.units_moves_queue.empty():
                active_unit = self.units_moves_queue.get()
                if active_unit not in units:
                    active_unit = None
            else:
                print('All units are dead')
                break
        return active_unit

    def analise(self):
        for unit_data in self.player_data["units"]:
            print(f'{bcolors.OKCYAN}{unit_data["unit_name"]}{bcolors.ENDC}, type - {unit_data["unit_type"]}. {bcolors.OKCYAN}HP - {unit_data["unit_hp"]}, '
                  f'DMG - {unit_data["unit_dmg"]}, DODGE - {unit_data["unit_dodge"]}{bcolors.ENDC}')





