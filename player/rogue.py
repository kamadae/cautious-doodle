from .base import Player
from ability import SneakAttack, Backstab, DodgeRoll, SmokeBomb, PoisonDagger


class Rogue(Player):
    """Rogue subclass with stealth."""

    def __init__(self, name):
        abilities = [SneakAttack(), Backstab(), PoisonDagger(), SmokeBomb(), DodgeRoll()]
        super().__init__(name, abilities=abilities)
        self.stealth = 5
