"""Automated tests for character creation and progression."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.player import Player
from utils.constants import Background

def test_character_background():
    p = Player(name="Kaelen", background=Background.SOLDIER.value)
    p.apply_background()
    assert p.attributes.strength == 7
    assert p.skills.firearms == 4
    assert p.derived.max_health == 165
    print("✅ test_character_background passed!")

def test_xp_leveling():
    p = Player()
    leveled = p.gain_xp(150)
    assert leveled is True
    assert p.level == 2
    assert p.stat_points == 2
    assert p.skill_points == 3
    print("✅ test_xp_leveling passed!")

if __name__ == "__main__":
    test_character_background()
    test_xp_leveling()
