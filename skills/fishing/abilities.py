from ability.base import Ability
from inventory.resources import RawFish


class HarpoonCast(Ability):
    """Catch a fish with a quick throw of the harpoon."""

    def __init__(self):
        super().__init__("Harpoon Cast")

    def use(self, user, target=None):
        fish = RawFish()
        if hasattr(user, "add_item"):
            user.add_item(fish)
        if hasattr(user, "skills") and "fishing" in user.skills:
            user.skills["fishing"].add_xp(10)
        return fish


class NetSweep(Ability):
    """Sweep a net to haul in extra fish."""

    def __init__(self):
        super().__init__("Net Sweep", cooldown=1)

    def use(self, user, target=None):
        fish = RawFish()
        if hasattr(user, "add_item"):
            user.add_item(fish)
            user.add_item(RawFish())  # two fish total
        if hasattr(user, "skills") and "fishing" in user.skills:
            user.skills["fishing"].add_xp(15)
        return fish

