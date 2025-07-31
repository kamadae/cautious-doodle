from .item import Item


class RawFish(Item):
    """Simple fish gathered from fishing."""

    def __init__(self):
        super().__init__("Raw Fish", weight=1)


class WoodLog(Item):
    """Log gathered from chopping trees."""

    def __init__(self):
        super().__init__("Wood Log", weight=2)


class BigFish(Item):
    """Larger fish found in deeper waters."""

    def __init__(self):
        super().__init__("Big Fish", weight=2)


class HardwoodLog(Item):
    """Stronger log gathered from tougher trees."""

    def __init__(self):
        super().__init__("Hardwood Log", weight=3)


class CommonHerb(Item):
    """Basic herb used in alchemy."""

    def __init__(self):
        super().__init__("Common Herb", weight=1)


class RareHerb(Item):
    """High-tier herb for advanced alchemy."""

    def __init__(self):
        super().__init__("Rare Herb", weight=1)


class CopperCoin(Item):
    """Low value currency for bartering."""

    def __init__(self):
        super().__init__("Copper Coin", weight=0)


class SilverCoin(Item):
    """Higher value currency for bartering."""

    def __init__(self):
        super().__init__("Silver Coin", weight=0)


class ClothScrap(Item):
    """Base material for crafting."""

    def __init__(self):
        super().__init__("Cloth Scrap", weight=1)


class FineCloth(Item):
    """Quality fabric for advanced crafting."""

    def __init__(self):
        super().__init__("Fine Cloth", weight=1)


class SimpleLockpick(Item):
    """Cheap lockpick for beginner thieves."""

    def __init__(self):
        super().__init__("Simple Lockpick", weight=0)


class MasterLockpick(Item):
    """High-quality lockpick for difficult locks."""

    def __init__(self):
        super().__init__("Master Lockpick", weight=0)


class IronOre(Item):
    """Common ore used in smithing."""

    def __init__(self):
        super().__init__("Iron Ore", weight=3)


class SteelIngot(Item):
    """Refined metal ingot for high-end smithing."""

    def __init__(self):
        super().__init__("Steel Ingot", weight=3)


class InspirationScroll(Item):
    """Scroll that improves speech skill when consumed."""

    def __init__(self):
        super().__init__("Inspiration Scroll", weight=1)


class OratoryManual(Item):
    """Advanced manual for great speakers."""

    def __init__(self):
        super().__init__("Oratory Manual", weight=2)


class SmokeBomb(Item):
    """Basic tool to aid stealth."""

    def __init__(self):
        super().__init__("Smoke Bomb", weight=1)


class CamouflageCloak(Item):
    """Higher tier stealth item."""

    def __init__(self):
        super().__init__("Camouflage Cloak", weight=2)


class AnimalPelt(Item):
    """Proof of tracking success."""

    def __init__(self):
        super().__init__("Animal Pelt", weight=2)


class RarePelt(Item):
    """Valuable pelt from elusive creatures."""

    def __init__(self):
        super().__init__("Rare Pelt", weight=2)

