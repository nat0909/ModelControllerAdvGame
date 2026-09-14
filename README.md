# ModelControllerAdvGame

A text-based adventure game built in Python, structured around a model/controller. You create a character, then fight enemies on a one-dimensional board diplayed by ASCII.

> [!NOTE]
> **This project is a work in progress and is not yet playable.** Character creation
> runs, and much of the combat model exists, but the game loop is not wired up —
> `game/main.py` does nothing, and the player's turn is still a stub. Running the
> game will not start a playable session yet.

## Project structure

- `game/` — entry point (`main.py`)
- `model/` — game logic, independent of how the game is displayed
  - `creature.py` — base stats shared by every creature
  - `character.py` — the player's character
  - `enemy.py`, `goblin.py` — enemies and their turn behavior
  - `scenario.py` — the state of a single encounter (positions, participants, HP)
  - `battle_engine.py` — attack rolls, damage, and healing
  - `turn_log.py` — a record of what happened on a turn
  - `helper_functions.py` — shared utilities
- `controller/` — user input and terminal output
  - `character_creation.py` — the character creation flow
  - `scenario_controller.py` — drives an encounter and renders the board
  - `formatting.py` — terminal formatting helpers
- `tests/` — pytest suite
- `data/` — reference notes, including [stat definitions](data/INFO.md)
- `saves/` — saved character data

## Game concepts

Creatures are defined by a small set of stats (described in [data/INFO.md](data/INFO.md)):

| Stat | Effect |
| --- | --- |
| Max Hit Points | When current HP reaches 0, the creature dies |
| Dexterity | Subtracted from attacks against the creature, making it harder to hit |
| Speed | How many spaces the creature can move in a turn |
| Melee Accuracy / Damage | Attack rolls and damage at adjacent range |
| Ranged Accuracy / Damage | Attack rolls and damage from a distance |

Characters choose one of three classes — **Warrior**, **Ranger**, or **Rogue** —
which adjust those base stats.

Combat takes place on a numbered line of spaces which is diplayed using ASCII. Each creature occupies one space. Creatures can move along the line, and if within range, perform a melee or ranged attack.
