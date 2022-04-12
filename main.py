from Game import Game
from bcolors import bcolors

game_settings = {}
settings = input(f'Choose game settings: {bcolors.OKGREEN}standard{bcolors.ENDC} or {bcolors.OKGREEN}custom{bcolors.ENDC}: ')
while settings not in ['standard', 'custom']:
    print(f'Choose between {bcolors.OKGREEN}standard{bcolors.ENDC} or {bcolors.OKGREEN}custom{bcolors.ENDC} settings')
    settings = input('Choose game settings: ')

if settings.lower() == 'standard':
    game_settings = {
        'multiplayer': False,
        'players_quantity': 2,
        'squad_size': 3,
        'difficulty': 'easy',
        'available_units': ['archer', 'wizard', 'swordsman']
    }
else:
    players_quantity = int(input('Choose how many players do you want: '))
    game_settings = {
        'multiplayer': False,
        'players_quantity': players_quantity,
        'squad_size': 3,
        'difficulty': 'easy',
        'available_units': ['archer', 'wizard', 'swordsman']
    }

local_game = Game()
local_game.set_settings(game_settings)
if not local_game.multiplayer:
    local_game.run()
