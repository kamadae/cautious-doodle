from .base import Ability


class Backstab(Ability):
    """High damage attack when used from stealth."""

    def __init__(self):
        super().__init__("Backstab", cooldown=2)
        self.base_damage = 8

    def can_use(self, user, target=None):
        return True

    def use(self, user, target):
        dmg = self.base_damage + user.attack_power
        if getattr(user, "stealth", 0) > 0:
            dmg += user.stealth * 2
        target.hp -= dmg
        return True
