from UnitInterface import Unit


class Swordsman(Unit):
    def __init__(self, hp=15, dmg=5, dodge=60):
        super().__init__()
        self.unit_params = {
            'HP': hp,
            'DMG': dmg,
            'DODGE': dodge
        }
