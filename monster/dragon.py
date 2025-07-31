from .base import Monster


class Dragon(Monster):
    """Boss monster with multi-phase behavior."""

    def __init__(self):
        super().__init__("Dragon", level=5, hp=100, attack=15, xp_reward=100)

    def attack(self, target):
        super().attack(target)
