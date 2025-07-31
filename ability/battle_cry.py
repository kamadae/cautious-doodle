from .base import Ability


class BattleCry(Ability):
    """Rally yourself to increase attack power."""

    def __init__(self):
        super().__init__("Battle Cry", cooldown=3)
        self.bonus = 5

    def use(self, user, target=None):
        user.attack_power += self.bonus
        return True
