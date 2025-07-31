from .base import Ability


class SmokeBomb(Ability):
    """Increase stealth for a short time."""

    def __init__(self):
        super().__init__("Smoke Bomb", cooldown=3)
        self.bonus = 3

    def use(self, user, target=None):
        current = getattr(user, "stealth", 0)
        setattr(user, "stealth", current + self.bonus)
        return True
