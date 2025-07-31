from .base import Player
from ability import PowerStrike, ShieldBash, Whirlwind, BattleCry


class Warrior(Player):
    """Warrior subclass with extra HP."""

    def __init__(self, name):
        abilities = [PowerStrike(), ShieldBash(), Whirlwind(), BattleCry()]
        super().__init__(name, hp=120, abilities=abilities)
