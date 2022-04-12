from Game import Game

game_settings = {}
settings = input('Choose game settings: standard or custom: ')
while settings not in ['standard', 'custom']:
    print('Choose between standard or custom settings')
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
    pass

local_game = Game()
local_game.set_settings(game_settings)
if not local_game.multiplayer:
    local_game.run()
