from .base import Ability


class PoisonDagger(Ability):
    """Strike with a blade coated in poison."""

    def __init__(self):
        super().__init__("Poison Dagger", cooldown=2)
        self.damage = 6

    def use(self, user, target):
        target.hp -= self.damage
        setattr(target, "poisoned", True)
        return True
