from player.base import Player
from inventory.consumable import HealingPotion


def test_healing_potion_restores_hp():
    p = Player("Hero")
    p.hp = 50
    potion = HealingPotion(amount=30)
    p.add_item(potion)
    p.use_item(potion)
    assert p.hp == 80
    assert potion not in p.inventory
