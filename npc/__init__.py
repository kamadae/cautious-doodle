"""NPC registry setup."""

from .merchant import Merchant
from .quest_giver import QuestGiver
from .trainer import Trainer

__all__ = ["Merchant", "QuestGiver", "Trainer"]
