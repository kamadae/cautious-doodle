class HUD:
    """Very small text-based HUD for the demo."""

    def render(self, player, area=None):
        """Print the player's vital stats to the console."""
        hp_bar = f"HP: {player.hp}/{player.max_hp}"
        xp_bar = f"LVL: {player.level} (XP {player.xp.total_xp})"
        pos_bar = f"Pos: ({player.x}, {player.y})"
        inv_bar = f"Items: {len(player.inventory)}"
        parts = [hp_bar, xp_bar, pos_bar, inv_bar]
        if area is not None:
            parts.append(f"Area: {area.name}")
        print(" | ".join(parts))
