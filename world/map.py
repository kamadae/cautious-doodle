class MapGrid:
    """Simple tile matrix placeholder."""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [[None] * width for _ in range(height)]
