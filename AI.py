import random
from bcolors import bcolors
from PlayerInterface import Player


class AI(Player):
    def __init__(self, player_name: str, game_settings: dict):
        super().__init__(player_name)
        self.name = player_name
        self.squad_size = game_settings['squad_size']
        self.available_units = game_settings['available_units']

    def form_squad(self):
        for i in range(self.squad_size):
            unit_type = random.choice(self.available_units)
            unit_name = f'unit{i}'
            unit_obj = self.create_unit(unit_type)
            unit_data = {
                'unit_name': unit_name,
                'unit_type': unit_type,
                'unit_obj': unit_obj,
                'unit_hp': unit_obj.unit_params['HP'],
                'unit_dmg': unit_obj.unit_params['DMG'],
                'unit_dodge': unit_obj.unit_params['DODGE'],
            }
            self.player_data['units'].append(unit_data)
            self.player_data['squad_hp'] += unit_data['unit_hp']

    def make_move(self, players: list):
        result = {
            'action': None,
            'target_player': None,
            'target_unit': None,
            'value': None
        }
        action = self.choose_action()
        if action == 'heal':
            hp, healing_unit = self.heal()
            result['action'] = action
            result['target_player'] = self
            result['target_unit'] = healing_unit
            result['value'] = hp
        else:
            enemy_player, target_unit, dmg = self.attack(players)
            result['action'] = action
            result['target_player'] = enemy_player
            result['target_unit'] = target_unit
            result['value'] = dmg
        return result

    def attack(self, players: list) -> tuple:
        target_player = self.choose_target_player(players)
        player_units = {}
        for unit_data in target_player.player_data['units']:
            player_units[unit_data['unit_name']] = unit_data['unit_obj']
        target_unit = random.choice(list(player_units.keys()))
        active_unit = self.get_alive_unit()
        print(
            f'{bcolors.OKBLUE}{self.player_data["player_name"]} attacking {target_player.player_data["player_name"]}{bcolors.ENDC}')
        if active_unit.attack(player_units[target_unit]):
            dmg = active_unit.unit_params['DMG']
            print(
                f'{bcolors.OKBLUE}Success attack. {target_player.player_data["player_name"] + "s"} {target_unit} receive {dmg} dmg{bcolors.ENDC}')
        else:
            dmg = 0
            print(
                f'{bcolors.OKBLUE}Unsuccessful attack. {target_player.player_data["player_name"] + "s"} {target_unit} receive {dmg} dmg{bcolors.ENDC}')

        self.units_moves_queue.put(active_unit)
        return target_player, target_unit, dmg

    def heal(self) -> tuple:
        alive_unit = self.get_alive_unit()
        if alive_unit:
            for unit_data in self.player_data['units']:
                if alive_unit == unit_data['unit_obj']:
                    hp = unit_data['unit_obj'].heal(unit_data['unit_hp'])
                    print(f'{bcolors.OKBLUE}{self.player_data["player_name"]} healing {unit_data["unit_name"]} - {unit_data["unit_type"]}{bcolors.ENDC}')
                    self.units_moves_queue.put(alive_unit)
                    return hp, alive_unit
        else:
            print('Something wrong. Unit is None')

    def choose_target_player(self, players: list):
        enemy_target = random.choice([player for player in players if player != self])
        return enemy_target

    def choose_action(self):
        actions = ['attack', 'heal']
        decision = random.choice(actions)
        return decision


