from inventory.resources import (
    RawFish, BigFish, WoodLog, HardwoodLog,
    CommonHerb, RareHerb, CopperCoin, SilverCoin,
    ClothScrap, FineCloth, SimpleLockpick, MasterLockpick,
    IronOre, SteelIngot, InspirationScroll, OratoryManual,
    SmokeBomb, CamouflageCloak, AnimalPelt, RarePelt,
)


def test_resource_tiers_exist():
    items = [
        RawFish(), BigFish(),
        WoodLog(), HardwoodLog(),
        CommonHerb(), RareHerb(),
        CopperCoin(), SilverCoin(),
        ClothScrap(), FineCloth(),
        SimpleLockpick(), MasterLockpick(),
        IronOre(), SteelIngot(),
        InspirationScroll(), OratoryManual(),
        SmokeBomb(), CamouflageCloak(),
        AnimalPelt(), RarePelt(),
    ]
    assert all(hasattr(i, "name") for i in items)

