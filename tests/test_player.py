from player.base import Player
from monster.goblin import Goblin
from combat.system import CombatSystem

def test_player_init():
    p = Player("Hero")
    assert p.name == "Hero"


def test_player_gain_xp_and_level():
    p = Player("Hero")
    p.gain_xp(100)
    assert p.level == 2


def test_combat_battle_player_wins():
    p = Player("Hero", hp=50, attack=20)
    g = Goblin()
    combat = CombatSystem()
    winner = combat.battle(p, g)
    assert winner == "player"
    assert p.level >= 1
