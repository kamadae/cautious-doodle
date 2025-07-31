from .base import Monster


class Goblin(Monster):
    """Low-tier melee monster."""

    def __init__(self):
        super().__init__("Goblin", level=1, hp=30, attack=5, xp_reward=10)

    def attack(self, target):
        super().attack(target)
