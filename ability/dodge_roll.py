from .base import Ability


class DodgeRoll(Ability):
    """AGI-based evasion maneuver."""

    def __init__(self):
        super().__init__("Dodge Roll", cooldown=1)

    def use(self, user, target):
        """Mark the user as dodging for one turn."""
        setattr(user, "dodging", True)
        return True
