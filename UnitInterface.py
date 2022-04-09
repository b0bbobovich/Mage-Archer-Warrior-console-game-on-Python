import abc


class Unit:
    @abc.abstractmethod
    def __init__(self, hp=0, dmg=0, dodge=0):
        self.heal_param = 25
        self.unit_params = {
            'HP': hp,
            'DMG': dmg,
            'DODGE': dodge
        }

    @abc.abstractmethod
    def attack(self) -> int:
        return self.unit_params['DMG']

    @abc.abstractmethod
    def heal(self) -> int:
        self.unit_params['HP'] += self.unit_params['HP'] * (self.heal_param/100)
        return int(self.unit_params['HP'])

    @abc.abstractmethod
    def dodge(self) -> bool:
        dodge_res = False
        if self.unit_params['DODGE']:
            dodge_res = True
            return dodge_res



