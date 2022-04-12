import random
from queue import Queue
from bcolors import bcolors
from PlayerInterface import Player
from AI import AI
from User import User


class Game:
    def __init__(self):
        self.game_settings = None
        self.players_quantity = None
        self.multiplayer = None
        self.players_move_queue = Queue()
        self.players = []

    def set_settings(self, game_settings: dict):
        self.game_settings = game_settings
        self.players_quantity = game_settings['players_quantity']
        self.multiplayer = game_settings['multiplayer']

    def run(self):
        moves_counter = 0

        self.create_player()
        for _ in range(self.players_quantity-1):
            self.create_ai_player()

        fighters = ''
        for player in self.players:
            fighters += (player.player_data['player_name'] + ' vs ')
        print(f'{bcolors.BOLD}Starting fight{bcolors.ENDC} {bcolors.FAIL}{fighters[:-3]}{bcolors.ENDC}')

        while len(self.players) > 1:
            if self.players_move_queue.empty():
                self.form_players_moves_queue()
                moves_counter += 1
                print(f'{bcolors.WARNING}Turn {moves_counter}{bcolors.ENDC}')
            player = self.players_move_queue.get()
            print(f'{bcolors.OKGREEN}{player.player_data["player_name"]} moving{bcolors.ENDC}')
            self.new_turn(player)

        print(f'{bcolors.BOLD}Winner is {bcolors.ENDC}{bcolors.OKGREEN}{self.players[0].player_data["player_name"]}{bcolors.ENDC}')

    def new_turn(self, player: Player):
        result = player.make_move(self.players)
        self.update_players_data(result)

    def update_players_data(self, result: dict):
        action = result['action']
        target_player = result['target_player']
        target_unit = result['target_unit']
        value = result['value']

        for unit_data in target_player.player_data['units']:
            if unit_data['unit_obj'] == target_unit:
                if action == 'attack':
                    unit_data['unit_hp'] -= value
                    if unit_data['unit_hp'] <= 0:
                        target_player.player_data['units'].remove(unit_data)
                        break
                else:
                    unit_data['unit_hp'] = value
                    break

        if not target_player.player_data['units']:
            print(f'{target_player.player_data["player_name"]} lose the game. All units are dead')
            self.players.remove(target_player)

    def form_players_moves_queue(self):
        for player in self.players:
            self.players_move_queue.put(player)

    def create_player(self):
        user_name = input('Enter your name: ')
        user_player = User(user_name, self.game_settings)
        user_player.form_squad()
        self.players.append(user_player)

    def create_ai_player(self):
        with open('ai_nicknames.txt', 'r') as names_file:
            names = names_file.read().splitlines()
            ai_name = random.choice(names)
        ai_player = AI(ai_name, self.game_settings)
        ai_player.form_squad()
        self.players.append(ai_player)











