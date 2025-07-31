from .base import Player
from ability import Fireball, DodgeRoll, IceBolt, LightningStrike


class Mage(Player):
    """Mage subclass with spellbook."""

    def __init__(self, name):
        abilities = [Fireball(), IceBolt(), LightningStrike(), DodgeRoll()]
        super().__init__(name, abilities=abilities)
        self.mp = 10
