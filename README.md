# RPG Prototype

This repository contains a simple skeleton for an RPG project. Some
basic functionality has been implemented to demonstrate the core
gameplay loop.

Players are divided into classes (Mage, Rogue, Warrior) each with
unique abilities such as ``Fireball`` or ``Backstab``. The base ``Player``
class also grants common actions like ``First Aid`` for healing and
``Quick Strike`` for a fast attack. Subclasses add their own spells:
Mages can cast ``Ice Bolt`` or the stronger ``Lightning Strike``,
Rogues throw ``Smoke Bombs`` or strike with a ``Poison Dagger``, and
Warriors unleash ``Whirlwind`` or rally with ``Battle Cry``. The base
``Player`` class remains usable for tests and generic demos.

## Running the demo

Execute::

    python main.py

This will start a very small top-down demo. First you will be asked for
your character's name and class. Use ``WASD`` keys to move your hero
around a 5x5 grid. Pick up the potion lying on the
ground and walk into the goblin to trigger a battle. The combat plays
out automatically once an encounter occurs. Stepping on certain tiles
will transition you to another ``Area`` such as the interior of a
building before returning outside.

While moving, a simple text HUD displays your current HP, level,
inventory count, and current coordinates so you always know where you
are on the map. Press ``i`` at any time to list the items you have
collected.

## Playtesting

The demo is intentionally minimal so you can easily try out the core
systems. After starting the game, move to the right to pick up the
healing potion at ``(1, 0)``. Then walk down and right again to bump
into the goblin at ``(2, 2)``. Combat resolves automatically and you
will see messages describing the outcome. Feel free to adjust
``main.py`` or the monster stats to experiment with different
encounters.

## Running tests

The project uses `pytest`. Run all tests with::

    pytest -q

## Skills and Gathering

Players now start with the ``fishing`` and ``woodcutting`` skills. These
skills gain experience when using their related gathering abilities and
level up over time. For example, the ``Harpoon Cast`` ability grants XP
to the fishing skill and yields ``Raw Fish`` items, while ``Chop Tree``
grants woodcutting XP and provides ``Wood Log`` resources. Each skill
also defines a second tier of materials (such as ``Big Fish`` or
``Hardwood Log``) that can be used by more advanced crafting systems.

## Crafting and Consuming

Gathered materials are used by other skills to create better items. The
``alchemy`` skill brews ``HealingPotion`` objects from herbs, awarding XP and
removing the herbs from your inventory. The ``smithing`` skill forges
``Steel Ingot``s out of ``Iron Ore``. Crafting actions consume resources and
help those skills level up.

## Assets

The project ships with an ``assets`` folder containing ``sprites``,
``audio`` and ``fonts`` subdirectories. Add your own images (for
example ``hero.png`` or ``goblin.png``) to ``assets/sprites`` and any
sound effects or music to ``assets/audio``. The code simply references
these file names so you can swap in whatever art you like.
