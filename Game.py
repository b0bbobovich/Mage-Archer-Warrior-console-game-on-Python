import random
import time

from PlayerInterface import Player
from AI import AI
from User import User


class Game:
    def __init__(self):
        self.players_quantity = None
        self.multiplayer = None
        self.difficulty = None
        self.players = {}

    def set_settings(self, game_settings: dict):
        self.players_quantity = game_settings['players_quantity']
        self.multiplayer = game_settings['multiplayer']
        self.difficulty = game_settings['difficulty']

        #heal_param = 25

    def run(self):
        moves_counter = 0

        user_name = input('Enter your name: ')
        user_player = User(user_name)
        self.players[user_player] = user_player.squad_hp

        for _ in range(self.players_quantity-1):
            self.create_ai_player()

        while len(self.players) > 1:
            moves_counter += 1
            print(f'Turn {moves_counter}')
            for player in self.players:
                self.new_turn(player, self.players)

    def create_ai_player(self):
        start = time.time()
        with open('ai_nicknames.txt', 'r') as names_file:
            names = names_file.read().splitlines()
            ai_name = random.choice(names)
        print(f'file with names opening and reading {time.time()- start} sec')
        ai_player = AI(ai_name)
        self.players[ai_player] = ai_player.squad_hp

    def new_turn(self, player: Player, players):
        if issubclass(type(player), AI):
            player.act(players)






