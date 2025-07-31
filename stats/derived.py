class DerivedStats:
    """Calculates derived stats."""

    def __init__(self, base):
        self.base = base
        self.HP_MAX = base.STR * 10
        self.MP_MAX = base.INT * 10
