from UnitInterface import Unit


class Swordsman(Unit):
    def __init__(self, hp=15, dmg=5, dodge=60):
        self.unit_params = {
            'HP': hp,
            'DMG': dmg,
            'DODGE': dodge
        }

    def attack(self) -> int:
        return self.unit_params['DMG']

    def heal(self) -> int:
        self.unit_params['HP'] += self.unit_params['HP'] * (self.heal_param/100)
        return int(self.unit_params['HP'])

    def dodge(self) -> bool:
        dodge_res = False
        if self.unit_params['DODGE']:
            dodge_res = True
            return dodge_res
