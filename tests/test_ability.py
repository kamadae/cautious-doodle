from ability.base import Ability
from ability import (
    FirstAid,
    QuickStrike,
    IceBolt,
    SmokeBomb,
    Whirlwind,
    LightningStrike,
    PoisonDagger,
    BattleCry,
)
from player.mage import Mage
from player.rogue import Rogue
from player.warrior import Warrior
from monster.goblin import Goblin

def test_ability_can_use():
    a = Ability("Test")
    assert a.can_use(None)


def test_first_aid_heals():
    p = Warrior("T")
    p.hp = 40
    FirstAid().use(p)
    assert p.hp > 40


def test_quick_strike_damages():
    p = Warrior("T")
    g = Goblin()
    QuickStrike().use(p, g)
    assert g.hp < 50  # goblin default hp is 50


def test_ice_bolt_applies_slow():
    m = Mage("M")
    g = Goblin()
    IceBolt().use(m, g)
    assert getattr(g, "slowed", False)


def test_smoke_bomb_increases_stealth():
    r = Rogue("R")
    before = r.stealth
    SmokeBomb().use(r)
    assert r.stealth > before


def test_whirlwind_stuns():
    w = Warrior("W")
    g = Goblin()
    Whirlwind().use(w, g)
    assert getattr(g, "stunned", False)


def test_lightning_strike_shocks():
    m = Mage("M")
    g = Goblin()
    LightningStrike().use(m, g)
    assert getattr(g, "shocked", False)


def test_poison_dagger_poison():
    r = Rogue("R")
    g = Goblin()
    PoisonDagger().use(r, g)
    assert getattr(g, "poisoned", False)


def test_battle_cry_increases_attack():
    w = Warrior("W")
    before = w.attack_power
    BattleCry().use(w)
    assert w.attack_power > before
