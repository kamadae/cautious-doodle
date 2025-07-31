from combat.system import CombatSystem
from .area import Area


class WorldManager:
    """Manage multiple areas and handle movement/encounters."""

    def __init__(self, width=5, height=5):
        # create a default starting area for backwards compatibility
        self.areas = {}
        start = Area("start", width, height)
        self.add_area(start, is_start=True)

    # ------------------------------------------------------------------
    # area/management helpers
    def add_area(self, area, is_start=False):
        self.areas[area.name] = area
        if is_start or not hasattr(self, "current_area"):
            self.current_area = area

    def add_item(self, item, x, y, area=None):
        area = area or self.current_area
        area.add_item(item, x, y)

    def add_monster(self, monster, x, y, area=None):
        area = area or self.current_area
        area.add_monster(monster, x, y)

    # ------------------------------------------------------------------
    def item_at(self, x, y, area=None):
        area = area or self.current_area
        return area.item_at(x, y)

    def monster_at(self, x, y, area=None):
        area = area or self.current_area
        return area.monster_at(x, y)

    def move_player(self, player, dx, dy):
        """Move ``player`` within the current area, handling exits."""
        area = self.current_area
        new_x = min(max(player.x + dx, 0), area.width - 1)
        new_y = min(max(player.y + dy, 0), area.height - 1)

        player.x = new_x
        player.y = new_y

        # handle area transitions first
        if (new_x, new_y) in area.exits:
            target_area, target_pos = area.exits[(new_x, new_y)]
            self.current_area = target_area
            player.x, player.y = target_pos
            area = target_area

        item = self.item_at(player.x, player.y, area)
        if item:
            player.add_item(item)
            area.items.remove(item)
            item.position = None

        monster = self.monster_at(player.x, player.y, area)
        if monster:
            print(f"Encounter! {player.name} meets {monster.name}!")
            winner = CombatSystem().battle(player, monster)
            if winner == "player":
                print(f"{player.name} defeated the {monster.name}!")
                area.monsters.remove(monster)
            else:
                print(f"{player.name} was defeated by the {monster.name}...")

