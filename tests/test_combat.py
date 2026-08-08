"""Automated tests for combat mechanics."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.combat import CombatEngine
from game.player import Player

def test_combat_loop():
    engine = CombatEngine("/opt/data/starveil-rpg/data/enemies.json")
    enemy = engine.create_enemy("aegis_security_guard")
    player = Player(name="Kaelen")

    assert enemy['current_health'] == 45
    msg = engine.execute_player_attack(player, enemy, is_aimed=True)
    assert len(msg) > 0
    print("✅ test_combat_loop passed!")

if __name__ == "__main__":
    test_combat_loop()
