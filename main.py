"""Entry point for the RPG project."""

from monster.goblin import Goblin
from player.mage import Mage
from player.rogue import Rogue
from player.warrior import Warrior
from inventory.consumable import HealingPotion
from world.world import WorldManager
from gui import HUD, ScreenManager, Menu


def create_player():
    """Ask the user for a name and class and return the new Player."""
    name = input("Enter your character name: ") or "Hero"
    menu = Menu("Choose your class", ["Mage", "Rogue", "Warrior"])
    choice = menu.open()
    if choice == 0:
        return Mage(name)
    if choice == 1:
        return Rogue(name)
    return Warrior(name)


def main():
    """Run a small top-down demo with one monster and one item."""
    world = WorldManager(5, 5)
    player = create_player()
    hud = HUD()
    screens = ScreenManager()
    screens.push(hud)
    potion = HealingPotion(amount=30)
    goblin = Goblin()

    world.add_item(potion, 1, 0)
    world.add_monster(goblin, 2, 2)

    print("Use WASD to move, q to quit")
    # continue until player dies or there are no monsters left in the current
    # area
    while player.is_alive() and world.current_area.monsters:
        cmd = input("Move: ").strip().lower()
        if cmd == "q":
            break
        dx = dy = 0
        if cmd == "w":
            dy = -1
        elif cmd == "s":
            dy = 1
        elif cmd == "a":
            dx = -1
        elif cmd == "d":
            dx = 1
        else:
            print("Invalid command")
            continue
        world.move_player(player, dx, dy)
        current = screens.current()
        if hasattr(current, "render"):
            current.render(player, world.current_area)
    print("Game over")


if __name__ == "__main__":
    main()
