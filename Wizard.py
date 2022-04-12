from UnitInterface import Unit


class Wizard(Unit):
    def __init__(self, hp=8, dmg=10, dodge=30):
        super().__init__()
        self.unit_params = {
            'HP': hp,
            'DMG': dmg,
            'DODGE': dodge
        }

