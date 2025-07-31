from .base import Ability


class Whirlwind(Ability):
    """Powerful spinning attack."""

    def __init__(self):
        super().__init__("Whirlwind", cooldown=3)
        self.multiplier = 1.2

    def use(self, user, target):
        dmg = int(user.attack_power * self.multiplier)
        target.hp -= dmg
        setattr(target, "stunned", True)
        return True
