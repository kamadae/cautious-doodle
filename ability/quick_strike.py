from .base import Ability


class QuickStrike(Ability):
    """Fast attack with minimal cooldown."""

    def __init__(self):
        super().__init__("Quick Strike", cooldown=0)

    def use(self, user, target):
        target.hp -= user.attack_power
        return True
