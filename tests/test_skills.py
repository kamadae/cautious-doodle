from skills.base import Skill
from skills.fishing import HarpoonCast
from inventory.resources import RawFish
from player.base import Player
from inventory.resources import CommonHerb, IronOre


def test_skill_level_up():
    s = Skill()
    s.add_xp(s.xp_to_next())
    assert s.level == 2


def test_harpoon_cast_gathers_fish():
    player = Player("Fisher")
    ability = HarpoonCast()
    ability.use(player)
    assert any(isinstance(i, RawFish) for i in player.inventory)
    assert player.skills["fishing"].xp > 0


def test_brew_potion_consumes_herb():
    player = Player("Alchemist")
    herb = CommonHerb()
    player.add_item(herb)
    potion = player.skills["alchemy"].brew_potion(player)
    assert potion is not None
    from inventory.consumable import HealingPotion
    assert isinstance(potion, HealingPotion)
    assert all(not isinstance(i, CommonHerb) for i in player.inventory)
    assert player.skills["alchemy"].xp > 0


def test_forge_ingot_consumes_ore():
    player = Player("Smith")
    ore = IronOre()
    player.add_item(ore)
    ingot = player.skills["smithing"].forge_ingot(player)
    from inventory.resources import SteelIngot
    assert isinstance(ingot, SteelIngot)
    assert all(not isinstance(i, IronOre) for i in player.inventory)
    assert player.skills["smithing"].xp > 0
