class Item:
    def __init__(self, name, weight=0, position=None):
        self.name = name
        self.weight = weight
        self.stackable = False
        # optional (x, y) position in the world
        self.position = position
