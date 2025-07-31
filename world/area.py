class Area:
    """Represents a rectangular map area."""

    def __init__(self, name, width=5, height=5):
        self.name = name
        self.width = width
        self.height = height
        self.items = []
        self.monsters = []
        # mapping ``(x, y)`` -> ``(target_area, target_pos)``
        self.exits = {}

    # ------------------------------------------------------------------
    # entity management helpers
    def add_item(self, item, x, y):
        item.position = (x, y)
        self.items.append(item)

    def add_monster(self, monster, x, y):
        monster.x = x
        monster.y = y
        self.monsters.append(monster)

    def item_at(self, x, y):
        for item in self.items:
            if item.position == (x, y):
                return item
        return None

    def monster_at(self, x, y):
        for monster in self.monsters:
            if (monster.x, monster.y) == (x, y):
                return monster
        return None

    def add_exit(self, x, y, target_area, target_pos=(0, 0)):
        """Create a transition from this area to ``target_area``."""
        self.exits[(x, y)] = (target_area, target_pos)

