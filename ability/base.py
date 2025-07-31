class Ability:
    """Base ability interface.

    Abilities are simple actions that entities can use in combat. Each
    ability exposes a :py:meth:`use` method which performs the action on a
    target.
    """

    def __init__(self, name, cooldown=0):
        self.name = name
        self.cooldown = cooldown

    # ------------------------------------------------------------------
    def can_use(self, user, target=None):
        """Return ``True`` if ``user`` is able to use this ability."""
        return True

    def use(self, user, target):
        """Apply the ability's effect.

        Subclasses should override this to implement their behaviour and
        return ``True`` when successfully executed.
        """
        raise NotImplementedError

    def trigger_cooldown(self):
        """Placeholder for cooldown logic."""
        pass
