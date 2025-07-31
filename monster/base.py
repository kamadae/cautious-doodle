class Monster:
    """Base monster class with simple combat stats."""

    def __init__(self, name, level=1, hp=50, attack=5, xp_reward=20, x=0, y=0):
        self.name = name
        self.level = level
        self.hp = hp
        self.attack_power = attack
        self.xp_reward = xp_reward
        # world position
        self.x = x
        self.y = y

    def is_alive(self):
        return self.hp > 0

    def attack(self, target):
        """Perform a basic attack."""
        target.hp -= self.attack_power

    def position(self):
        return (self.x, self.y)
