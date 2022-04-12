from PlayerInterface import Player
from bcolors import bcolors


class User(Player):
    def __init__(self, player_name: str, game_settings: dict):
        super().__init__(player_name)
        self.name = player_name
        self.squad_size = game_settings['squad_size']
        self.available_units = game_settings['available_units']

    def form_squad(self):
        print(f'Choose {self.squad_size} characters between {self.available_units}')
        for i in range(self.squad_size):
            unit_type = input(f'Choose {i} unit: ').lower()
            while unit_type not in self.available_units:
                print('Choose between available characters')
                unit_type = input(f'Choose {i} unit: ').lower()

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

    def make_move(self, players: list) -> dict:
        result = {
            'action': None,
            'target_player': None,
            'target_unit': None,
            'value': None
        }
        print(f'{bcolors.FAIL}My squad stats: {bcolors.ENDC}')
        self.analise()
        action = input(f'Choose action: {bcolors.OKGREEN}heal{bcolors.ENDC} or {bcolors.FAIL}attack{bcolors.ENDC}: ')
        while action not in ['heal', 'attack']:
            print('Choose action between heal or attack')
            action = input('Choose action: heal or attack: ')
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
        enemies_players = {}
        for player in players:
            if player != self:
                enemies_players[player.player_data['player_name']] = player

        print(f'{bcolors.WARNING}Enemy stats: {bcolors.ENDC}')
        for enemy_name, enemy in enemies_players.items():
            print(f'Enemy: {enemy_name}')
            enemy.analise()

        target_player = input(f'Choose enemy: ')
        while target_player not in list(enemies_players.keys()):
            print('No such enemy')
            target_player = input('Choose between available enemies: ')

        target_player = enemies_players.get(target_player)
        player_units = {}
        for unit_data in target_player.player_data['units']:
            player_units[unit_data['unit_name']] = unit_data['unit_obj']
        target_unit_name = input('Choose enemy unit: ')

        while target_unit_name not in player_units:
            print('No such unit in enemy squad')
            target_unit_name = input('Choose available enemy unit: ')

        target_unit = player_units.get(target_unit_name)
        active_unit = self.get_alive_unit()
        if active_unit.attack(player_units[target_unit_name]):
            dmg = active_unit.unit_params['DMG']
            print(f'{bcolors.OKBLUE}Success attack. {target_player.player_data["player_name"] + "s"} {target_unit_name} receive {dmg} dmg{bcolors.ENDC}')
        else:
            dmg = 0
            print(f'{bcolors.OKBLUE}Unsuccessful attack. {target_player.player_data["player_name"] + "s"} {target_unit_name} receive {dmg} dmg{bcolors.ENDC}')
        self.units_moves_queue.put(active_unit)
        return target_player, target_unit, dmg

    def heal(self) -> tuple:
        alive_unit = self.get_alive_unit()
        if alive_unit:
            for unit_data in self.player_data['units']:
                if alive_unit == unit_data['unit_obj']:
                    hp = unit_data['unit_obj'].heal(unit_data['unit_hp'])
                    self.units_moves_queue.put(alive_unit)
                    return hp, alive_unit
        else:
            print('Something wrong. Unit is None')


