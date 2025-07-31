from .base import Ability


class Fireball(Ability):
    """Simple magic attack costing MP."""

    def __init__(self):
        super().__init__("Fireball", cooldown=2)
        self.damage = 12
        self.cost = 5

    def can_use(self, user, target=None):
        return getattr(user, "mp", 0) >= self.cost

    def use(self, user, target):
        if not self.can_use(user, target):
            return False
        user.mp -= self.cost
        target.hp -= self.damage
        return True
