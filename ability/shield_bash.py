from .base import Ability


class ShieldBash(Ability):
    """Defensive attack for warriors."""

    def __init__(self):
        super().__init__("Shield Bash", cooldown=1)
        self.bonus = 3

    def use(self, user, target):
        dmg = user.attack_power + self.bonus
        target.hp -= dmg
        # grant user a temporary defense boost
        user.hp = min(user.max_hp, user.hp + 2)
        return True
