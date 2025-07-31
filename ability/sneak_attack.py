from .base import Ability


class SneakAttack(Ability):
    """Stealth-based rogue attack."""

    def __init__(self):
        super().__init__("Sneak Attack", cooldown=1)
        self.base_damage = 5

    def use(self, user, target):
        dmg = self.base_damage + user.attack_power
        if getattr(user, "stealth", 0) > 0:
            dmg += user.stealth
        target.hp -= dmg
        return True
