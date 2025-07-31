from .base import Ability


class IceBolt(Ability):
    """Magic attack that slows the target."""

    def __init__(self):
        super().__init__("Ice Bolt", cooldown=2)
        self.damage = 8
        self.cost = 4

    def can_use(self, user, target=None):
        return getattr(user, "mp", 0) >= self.cost

    def use(self, user, target):
        if not self.can_use(user, target):
            return False
        user.mp -= self.cost
        target.hp -= self.damage
        setattr(target, "slowed", True)
        return True
