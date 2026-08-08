"""Branching dialogue tree manager for Starveil RPG."""

import json
from game.player import Player
from game.skill_checks import SkillCheckSystem

class DialogueManager:
    def __init__(self, dialogue_file: str):
        with open(dialogue_file, 'r') as f:
            self.dialogue_db = json.load(f)

    def get_node(self, npc_id: str, node_id: str = "start") -> dict:
        npc_dialogue = self.dialogue_db.get(npc_id, {})
        return npc_dialogue.get(node_id, {})

    def evaluate_options(self, player: Player, options: list[dict]) -> list[dict]:
        """Filters options and checks background/skill prerequisites."""
        available = []
        for opt in options:
            req_bg = opt.get('background_req')
            if req_bg and player.background != req_bg:
                continue
            available.append(opt)
        return available
