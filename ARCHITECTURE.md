# System Architecture — STARVEIL: SHADOWS OF THE SECTOR

## 🏗️ Overview
STARVEIL is engineered with a modular, decoupled Python architecture designed for data-driven expansion.

```
starveil-rpg/
├── main.py                     # CLI Game Entry Point
├── index.html                  # HTML5 Retro Terminal Web Engine
├── game/                       # Core Python RPG Systems
│   ├── game.py                 # Master Controller (GameEngine)
│   ├── player.py               # Player Model & Progression
│   ├── character.py            # Attributes & Derived Combat Stats
│   ├── skills.py               # Skill & Attribute Definitions
│   ├── skill_checks.py         # Generalized Skill Roll Calculator
│   ├── combat.py               # Tactical Turn-Based Combat Engine
│   ├── dialogue.py             # Branching Dialogue Trees
│   ├── quests.py               # Quest Framework & Tracker
│   ├── factions.py             # Faction Reputation System
│   ├── world.py                # World, Systems, & Locations Manager
│   ├── travel.py               # Interstellar Spacecraft Travel Engine
│   ├── inventory.py            # Inventory, Equipment & Consumables
│   ├── companions.py           # Recruitable Companions
│   ├── save_system.py          # Save/Load & Autosave Engine
│   └── ai_gm.py                # Google Gemini API AI Game Master Wrapper
├── data/                       # Data-Driven Content Files (JSON)
│   ├── factions.json
│   ├── items.json
│   ├── weapons.json
│   ├── enemies.json
│   ├── locations.json
│   ├── quests.json
│   ├── dialogue.json
│   └── encounters.json
├── utils/                      # Reusable Utilities
│   ├── constants.py
│   ├── input_utils.py
│   └── display_utils.py
└── tests/                      # Automated Unit & System Tests
    ├── test_character.py
    ├── test_combat.py
    └── test_save.py
```

## 🔄 Core Data Flow
1. **Content Isolation:** All location descriptions, dialogue trees, enemies, weapons, and quests are defined in `data/*.json` files.
2. **State Management:** `GameEngine` acts as the single source of truth for player state, world coordinates, quest flags, and reputation metrics.
3. **Save System:** Game state is serialized to lightweight JSON files in `saves/` (or `localStorage` in web mode).
