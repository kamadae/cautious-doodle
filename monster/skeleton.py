from .base import Monster


class Skeleton(Monster):
    """Mid-tier ranged monster."""

    def __init__(self):
        super().__init__("Skeleton", level=2, hp=40, attack=7, xp_reward=20)

    def attack(self, target):
        super().attack(target)
