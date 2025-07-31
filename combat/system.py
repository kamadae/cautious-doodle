class CombatSystem:
    """Handles very basic turn-based combat."""

    def battle(self, player, monster):
        """Run a player vs monster battle.

        The player always attacks first. Returns the string ``"player"`` if
        the player wins or ``"monster"`` if defeated.
        """
        turn = 0
        while player.is_alive() and monster.is_alive():
            if turn % 2 == 0:
                player.attack(monster)
            else:
                monster.attack(player)
            turn += 1

        if player.is_alive():
            player.gain_xp(monster.xp_reward)
            return "player"
        return "monster"
