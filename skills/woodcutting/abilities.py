from ability.base import Ability
from inventory.resources import WoodLog


class ChopTree(Ability):
    """Chop down a tree to gather logs."""

    def __init__(self):
        super().__init__("Chop Tree")

    def use(self, user, target=None):
        log = WoodLog()
        if hasattr(user, "add_item"):
            user.add_item(log)
        if hasattr(user, "skills") and "woodcutting" in user.skills:
            user.skills["woodcutting"].add_xp(10)
        return log

