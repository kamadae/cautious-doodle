from ..base import Skill
from inventory import IronOre, SteelIngot


class Smithing(Skill):
    """Forge raw ore into steel ingots."""

    def forge_ingot(self, player):
        """Convert one ``Iron Ore`` in the player's inventory to a ``Steel Ingot``."""
        for item in list(player.inventory):
            if isinstance(item, IronOre):
                player.inventory.remove(item)
                ingot = SteelIngot()
                player.add_item(ingot)
                self.add_xp(20)
                return ingot
        return None
