class XPSystem:
    """Tracks experience points and handles level ups."""

    def __init__(self):
        self.total_xp = 0
        self.level = 1

    def add_xp(self, amount):
        """Add XP and increase level when thresholds are reached."""
        self.total_xp += amount
        leveled = False
        # simple exponential threshold: 100 xp per current level
        while self.total_xp >= self.level * 100:
            self.total_xp -= self.level * 100
            self.level += 1
            leveled = True
        return leveled
