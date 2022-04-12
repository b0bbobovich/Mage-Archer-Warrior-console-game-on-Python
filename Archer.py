from UnitInterface import Unit


class Archer(Unit):
    def __init__(self, hp=12, dmg=4, dodge=40):
        super().__init__()
        self.unit_params = {
            'HP': hp,
            'DMG': dmg,
            'DODGE': dodge
        }


