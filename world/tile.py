class Tile:
    """Map tile representation."""

    def __init__(self, sprite_ref, walkable=True):
        self.sprite_ref = sprite_ref
        self.walkable = walkable
