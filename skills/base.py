class Skill:
    """Base skill with experience and leveling."""

    def __init__(self):
        self.level = 1
        self.xp = 0

    # --------------------------------------------------------------
    def xp_to_next(self):
        """XP required for the next level."""
        return self.level * 50

    def add_xp(self, amount):
        """Increase XP and level up when the threshold is reached."""
        self.xp += amount
        leveled = False
        while self.xp >= self.xp_to_next():
            self.xp -= self.xp_to_next()
            self.level += 1
            leveled = True
            self.on_level_up()
        return leveled

    # --------------------------------------------------------------
    def on_level_up(self):
        """Hook called whenever the skill levels up."""
        pass
