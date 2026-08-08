"""Save/Load system for Starveil RPG."""

import json
import os
from game.player import Player

SAVE_DIR = "/opt/data/starveil-rpg/saves"

class SaveSystem:
    @staticmethod
    def ensure_save_dir():
        os.makedirs(SAVE_DIR, exist_ok=True)

    @staticmethod
    def save_game(player: Player, quest_manager, faction_system, filename: str = "save_slot_1.json") -> bool:
        SaveSystem.ensure_save_dir()
        filepath = os.path.join(SAVE_DIR, filename)

        save_data = {
            "player": player.to_dict(),
            "active_quests": quest_manager.active_quests,
            "completed_quests": quest_manager.completed_quests,
            "factions": {k: v['reputation'] for k, v in faction_system.factions.items()}
        }

        try:
            with open(filepath, 'w') as f:
                json.dump(save_data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving game: {e}")
            return False

    @staticmethod
    def load_game(filename: str = "save_slot_1.json") -> tuple[Player, dict, dict, dict] | None:
        filepath = os.path.join(SAVE_DIR, filename)
        if not os.path.exists(filepath):
            return None

        try:
            with open(filepath, 'r') as f:
                data = json.load(f)

            player = Player.from_dict(data.get("player", {}))
            active_quests = data.get("active_quests", {})
            completed_quests = data.get("completed_quests", {})
            factions_rep = data.get("factions", {})

            return player, active_quests, completed_quests, factions_rep
        except Exception as e:
            print(f"Error loading game: {e}")
            return None
