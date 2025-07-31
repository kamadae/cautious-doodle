from .item import Item


class Consumable(Item):
    """Base class for items that are consumed on use."""

    def use(self, target):
        """Apply the consumable's effect to ``target``.

        Subclasses should override this to implement their behavior.
        """
        pass


class HealingPotion(Consumable):
    """Simple potion that restores hit points."""

    def __init__(self, amount=20):
        super().__init__("Healing Potion", weight=0)
        self.amount = amount

    def use(self, target):
        target.heal(self.amount)
