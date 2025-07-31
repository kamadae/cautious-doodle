class HUD:
    """Very small text-based HUD for the demo."""

    def render(self, player):
        """Print the player's vital stats to the console."""
        hp_bar = f"HP: {player.hp}/{player.max_hp}"
        xp_bar = f"LVL: {player.level} (XP {player.xp.total_xp})"
        info = f"{hp_bar} | {xp_bar}"
        print(info)
