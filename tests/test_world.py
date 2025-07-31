from world.world import WorldManager
from world.area import Area
from player.base import Player
from monster.goblin import Goblin
from inventory.consumable import HealingPotion


def test_move_pickup_and_battle():
    world = WorldManager(5, 5)
    player = Player("Hero")
    potion = HealingPotion(amount=20)
    goblin = Goblin()

    world.add_item(potion, 0, 1)
    world.add_monster(goblin, 1, 0)

    # move to pick up potion
    world.move_player(player, 0, 1)
    assert potion in player.inventory

    # move into goblin to battle
    world.move_player(player, 1, -1)
    assert goblin not in world.current_area.monsters


def test_enter_building_and_exit():
    world = WorldManager(3, 3)
    player = Player("Hero")
    building = Area("house", 2, 2)
    world.add_area(building)
    # exit inside building back to start area
    building.add_exit(0, 0, world.current_area, (1, 1))
    # entrance from start area into building
    world.current_area.add_exit(1, 1, building, (0, 0))

    # move onto entrance tile -> should transition to building
    world.move_player(player, 1, 1)
    assert world.current_area is building
    # move back to exit -> should return to start
    world.move_player(player, 0, 0)  # staying in place triggers exit
    assert world.current_area.name == "start"

