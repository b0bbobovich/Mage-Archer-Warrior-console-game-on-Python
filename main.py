import random
from Game import Game
from PlayerInterface import Player
from AI import AI
from User import User

game_settings = {}
settings = input('Choose game settings: standard or custom: ')

if settings.lower() == 'standard':
    game_settings = {
        'multiplayer': False,
        'players_quantity': 2,
        'difficulty': 'medium'
    }
elif settings.lower() == 'custom':
    pass
else:
    print('Choose between standard or custom settings')

local_game = Game()
local_game.set_settings(game_settings)
if not local_game.multiplayer:
    local_game.run()
