from .base import Ability


class FirstAid(Ability):
    """Simple self heal ability."""

    def __init__(self):
        super().__init__("First Aid", cooldown=2)
        self.amount = 10

    def use(self, user, target=None):
        user.heal(self.amount)
        return True
