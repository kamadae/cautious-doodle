from .xp import XPSystem
from skills.fishing import Fishing
from skills.woodcutting import Woodcutting
from skills.alchemy import Alchemy
from skills.smithing import Smithing
from ability import FirstAid, QuickStrike


class Player:
    """Main player class with simple combat and progression."""

    def __init__(self, name, hp=100, attack=10, x=0, y=0, abilities=None):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_power = attack
        # world position
        self.x = x
        self.y = y
        self.inventory = []
        self.xp = XPSystem()
        base_abilities = [FirstAid(), QuickStrike()]
        self.abilities = (abilities or []) + base_abilities
        # initialise player skills
        self.skills = {
            "fishing": Fishing(),
            "woodcutting": Woodcutting(),
            "alchemy": Alchemy(),
            "smithing": Smithing(),
        }

    # convenience property
    @property
    def level(self):
        return self.xp.level

    def is_alive(self):
        return self.hp > 0

    def attack(self, target):
        target.hp -= self.attack_power

    def heal(self, amount):
        """Restore hit points up to ``max_hp``."""
        self.hp = min(self.max_hp, self.hp + amount)

    def position(self):
        return (self.x, self.y)

    def move(self, dx, dy, world=None):
        """Move the player by ``dx`` and ``dy`` within the given world."""
        if world is not None:
            world.move_player(self, dx, dy)
        else:
            self.x += dx
            self.y += dy

    def add_item(self, item):
        self.inventory.append(item)

    def use_item(self, item):
        if item in self.inventory:
            if hasattr(item, "use"):
                item.use(self)
                self.inventory.remove(item)

    def use_ability(self, ability, target):
        """Use an ability against a ``target`` if possible."""
        if ability in self.abilities and ability.can_use(self, target):
            return ability.use(self, target)
        return False

    def gain_xp(self, amount):
        """Add XP to the player's XP system."""
        return self.xp.add_xp(amount)
