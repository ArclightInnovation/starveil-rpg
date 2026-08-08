"""Skill check system for Starveil RPG."""

import random
from game.player import Player

class SkillCheckSystem:
    @staticmethod
    def perform_check(player: Player, skill_name: str, difficulty: int, bonus: int = 0) -> tuple[bool, str]:
        """Calculates success probability and performs roll."""
        skill_val = player.skills.get_skill(skill_name)
        
        # Link attribute bonus
        attr_map = {
            "firearms": "perception",
            "melee": "strength",
            "engineering": "technical",
            "hacking": "technical",
            "medicine": "intelligence",
            "piloting": "agility",
            "persuasion": "presence",
            "intimidation": "strength",
            "stealth": "agility",
            "science": "intelligence",
            "survival": "perception",
            "investigation": "perception"
        }
        
        attr_name = attr_map.get(skill_name.lower(), "intelligence")
        attr_val = player.attributes.get_attr(attr_name)

        total_score = skill_val + (attr_val // 2) + bonus
        roll = random.randint(1, 10)
        final_score = total_score + roll

        is_success = final_score >= difficulty
        
        detail_msg = f"[{skill_name.capitalize()} Check] Difficulty: {difficulty} | Skill+Bonus: {total_score} + Roll ({roll}) = {final_score}"
        return is_success, detail_msg
