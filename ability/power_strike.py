from .base import Ability


class PowerStrike(Ability):
    """STR-scaled warrior attack."""

    def __init__(self):
        super().__init__("Power Strike", cooldown=2)
        self.multiplier = 1.5

    def use(self, user, target):
        dmg = int(user.attack_power * self.multiplier)
        target.hp -= dmg
        return True
