import random


class Unit:
    def __init__(self):
        self.heal_param = 25

    def attack(self, target_unit) -> int:
        hit = False
        target_unit_dodge = target_unit.unit_params['DODGE']
        if random.randint(1, 101) < target_unit_dodge:
            hit = True
        return hit

    def heal(self, hp: int) -> int:
        hp += hp * (self.heal_param/100)
        return int(hp)




