from ..base import Skill
from inventory import HealingPotion, CommonHerb, RareHerb


class Alchemy(Skill):
    """Use herbs to brew healing potions."""

    def brew_potion(self, player, rare=False):
        """Consume a herb from ``player`` and create a potion.

        Returns the created potion or ``None`` if the player lacks herbs.
        """
        herb_cls = RareHerb if rare else CommonHerb
        for item in list(player.inventory):
            if isinstance(item, herb_cls):
                player.inventory.remove(item)
                amount = 50 if rare else 20
                potion = HealingPotion(amount=amount)
                player.add_item(potion)
                self.add_xp(30 if rare else 15)
                return potion
        return None
