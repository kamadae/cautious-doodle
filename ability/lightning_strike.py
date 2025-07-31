from .base import Ability


class LightningStrike(Ability):
    """Powerful spell that shocks the target."""

    def __init__(self):
        super().__init__("Lightning Strike", cooldown=3)
        self.damage = 15
        self.cost = 7

    def can_use(self, user, target=None):
        return getattr(user, "mp", 0) >= self.cost

    def use(self, user, target):
        if not self.can_use(user, target):
            return False
        user.mp -= self.cost
        target.hp -= self.damage
        setattr(target, "shocked", True)
        return True
