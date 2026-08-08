"""Turn-based tactical combat engine for Starveil RPG."""

import random
import json
from game.player import Player

class CombatEngine:
    def __init__(self, enemies_file: str):
        with open(enemies_file, 'r') as f:
            self.enemy_db = {e['id']: e for e in json.load(f)}

    def create_enemy(self, enemy_id: str) -> dict:
        if enemy_id in self.enemy_db:
            e = self.enemy_db[enemy_id].copy()
            e['current_health'] = e['health']
            return e
        raise ValueError(f"Enemy ID {enemy_id} not found.")

    def execute_player_attack(self, player: Player, enemy: dict, is_aimed: bool = False) -> str:
        weapon = player.equipped_weapon
        if weapon:
            dmg_min = weapon.get('damage_min', 10)
            dmg_max = weapon.get('damage_max', 18)
            base_acc = weapon.get('accuracy', 75)
            crit_rate = weapon.get('crit_chance', 5)
        else:
            # Unarmed
            dmg_min = 4
            dmg_max = 8
            base_acc = 70
            crit_rate = 5

        accuracy = base_acc + player.derived.accuracy // 10
        if is_aimed:
            accuracy += 20
            crit_rate += 15

        roll = random.randint(1, 100)
        if roll <= accuracy:
            raw_dmg = random.randint(dmg_min, dmg_max)
            # Check critical hit
            crit_roll = random.randint(1, 100)
            is_crit = crit_roll <= crit_rate
            if is_crit:
                raw_dmg = int(raw_dmg * 1.8)

            armor = enemy.get('armor', 0)
            actual_dmg = max(1, raw_dmg - armor)
            enemy['current_health'] -= actual_dmg

            crit_str = " CRITICAL HIT!" if is_crit else ""
            return f"You hit {enemy['name']} for {actual_dmg} damage!{crit_str} ({enemy['current_health']}/{enemy['health']} HP remaining)"
        else:
            return f"Your attack missed {enemy['name']}!"

    def execute_enemy_attack(self, enemy: dict, player: Player) -> str:
        dmg_min = enemy.get('damage_min', 6)
        dmg_max = enemy.get('damage_max', 12)
        acc = enemy.get('accuracy', 70)

        roll = random.randint(1, 100)
        # Check evasion
        effective_acc = max(10, acc - player.derived.evasion)

        if roll <= effective_acc:
            raw_dmg = random.randint(dmg_min, dmg_max)
            armor = player.derived.armor
            actual_dmg = max(1, raw_dmg - armor)
            player.derived.health -= actual_dmg
            return f"{enemy['name']} attacks you for {actual_dmg} damage! (Your HP: {player.derived.health}/{player.derived.max_health})"
        else:
            return f"{enemy['name']} attacks but misses you!"
