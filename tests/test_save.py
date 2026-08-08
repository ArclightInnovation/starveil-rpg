"""Automated tests for save/load mechanics."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.game import GameEngine
from game.save_system import SaveSystem

def test_save_load():
    engine = GameEngine()
    engine.create_character("TestHero", "Smuggler")
    engine.player.credits = 1250

    saved = SaveSystem.save_game(engine.player, engine.quest_mgr, engine.faction_sys, "test_slot.json")
    assert saved is True

    res = SaveSystem.load_game("test_slot.json")
    assert res is not None
    loaded_player, _, _, _ = res
    assert loaded_player.name == "TestHero"
    assert loaded_player.credits == 1250
    print("✅ test_save_load passed!")

if __name__ == "__main__":
    test_save_load()
