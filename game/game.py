"""Master Game State & Controller for Starveil RPG."""

import json
from game.player import Player
from game.character import Skills, Attributes
from game.inventory import InventoryManager
from game.factions import FactionSystem
from game.world import WorldManager
from game.travel import TravelManager
from game.combat import CombatEngine
from game.dialogue import DialogueManager
from game.quests import QuestManager
from game.save_system import SaveSystem
from game.ai_gm import AIGameMaster
from game.skill_checks import SkillCheckSystem
from utils.constants import Background, BACKGROUND_DESCRIPTIONS

class GameEngine:
    def __init__(self, data_dir: str = "/opt/data/starveil-rpg/data"):
        self.data_dir = data_dir
        self.inventory_mgr = InventoryManager(f"{data_dir}/items.json", f"{data_dir}/weapons.json")
        self.faction_sys = FactionSystem(f"{data_dir}/factions.json")
        self.world_mgr = WorldManager(f"{data_dir}/locations.json")
        self.travel_mgr = TravelManager(self.world_mgr)
        self.combat_engine = CombatEngine(f"{data_dir}/enemies.json")
        self.dialogue_mgr = DialogueManager(f"{data_dir}/dialogue.json")
        self.quest_mgr = QuestManager(f"{data_dir}/quests.json")
        self.ai_gm = AIGameMaster()
        self.player = Player()

    def create_character(self, name: str, background_str: str) -> Player:
        self.player = Player(name=name, background=background_str)
        self.player.apply_background()
        
        # Give starting gear
        self.inventory_mgr.add_item_by_id(self.player, "mag_pistol")
        self.inventory_mgr.equip_item(self.player, "mag_pistol")
        self.inventory_mgr.add_item_by_id(self.player, "nanite_injector")
        self.inventory_mgr.add_item_by_id(self.player, "aegis_weave_vest")
        self.inventory_mgr.equip_item(self.player, "aegis_weave_vest")

        return self.player

    def get_current_location_data(self) -> dict:
        return self.world_mgr.get_location(self.player.current_location_id)

    def trigger_location_narration(self) -> str:
        loc = self.get_current_location_data()
        prompt = f"The player {self.player.name} ({self.player.background}) arrives at {loc.get('name')}. Description: {loc.get('description')}."
        ai_narrative = self.ai_gm.generate_narration(prompt)
        if ai_narrative:
            return f"🌌 [AI Game Master]: {ai_narrative}"
        return f"{loc.get('description')}"

    def save_game_state(self, filename: str = "save_slot_1.json") -> bool:
        return SaveSystem.save_game(self.player, self.quest_mgr, self.faction_sys, filename)

    def load_game_state(self, filename: str = "save_slot_1.json") -> bool:
        res = SaveSystem.load_game(filename)
        if res:
            p, active_q, comp_q, facs = res
            self.player = p
            self.quest_mgr.active_quests = active_q
            self.quest_mgr.completed_quests = comp_q
            for k, v in facs.items():
                if k in self.faction_sys.factions:
                    self.faction_sys.factions[k]['reputation'] = v
            return True
        return False
