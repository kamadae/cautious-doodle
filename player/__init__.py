"""Player package."""

from .base import Player
from .mage import Mage
from .rogue import Rogue
from .warrior import Warrior

__all__ = ["Player", "Mage", "Rogue", "Warrior"]
