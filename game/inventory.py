"""Inventory and item management for Starveil RPG."""

import json
from game.player import Player

class InventoryManager:
    def __init__(self, items_file: str, weapons_file: str):
        with open(items_file, 'r') as f:
            self.items_db = {item['id']: item for item in json.load(f)}
        with open(weapons_file, 'r') as f:
            for w in json.load(f):
                self.items_db[w['id']] = w

    def add_item_by_id(self, player: Player, item_id: str) -> bool:
        if item_id in self.items_db:
            item = self.items_db[item_id]
            player.inventory_items.append(item)
            return True
        return False

    def equip_item(self, player: Player, item_id: str) -> tuple[bool, str]:
        for idx, item in enumerate(player.inventory_items):
            if item.get('id') == item_id:
                item_type = item.get('type')
                if item_type == 'weapon':
                    if player.equipped_weapon:
                        player.inventory_items.append(player.equipped_weapon)
                    player.equipped_weapon = item
                    player.inventory_items.pop(idx)
                    return True, f"Equipped weapon: {item['name']}"
                elif item_type == 'armor':
                    if player.equipped_armor:
                        player.inventory_items.append(player.equipped_armor)
                    player.equipped_armor = item
                    player.inventory_items.pop(idx)
                    
                    # Recalculate armor stats
                    armor_val = item.get('effects', {}).get('armor', 0)
                    player.derived.armor = armor_val
                    return True, f"Equipped armor: {item['name']}"
                elif item_type == 'tech_module':
                    if player.equipped_tech:
                        player.inventory_items.append(player.equipped_tech)
                    player.equipped_tech = item
                    player.inventory_items.pop(idx)
                    return True, f"Equipped tech module: {item['name']}"
                else:
                    return False, f"Item '{item['name']}' cannot be equipped."
        return False, "Item not found in inventory."

    def use_item(self, player: Player, item_id: str) -> tuple[bool, str]:
        for idx, item in enumerate(player.inventory_items):
            if item.get('id') == item_id and item.get('type') == 'consumable':
                effects = item.get('effects', {})
                msg_parts = []
                
                if 'heal' in effects:
                    heal_amt = effects['heal']
                    player.derived.health = min(player.derived.max_health, player.derived.health + heal_amt)
                    msg_parts.append(f"Restored {heal_amt} HP")
                
                if 'energy_restore' in effects:
                    energy_amt = effects['energy_restore']
                    player.derived.energy = min(player.derived.max_energy, player.derived.energy + energy_amt)
                    msg_parts.append(f"Restored {energy_amt} Energy")

                player.inventory_items.pop(idx)
                return True, f"Used {item['name']}: {', '.join(msg_parts)}"
        return False, "Consumable item not found."
