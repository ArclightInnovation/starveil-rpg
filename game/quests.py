"""Quest tracking framework for Starveil RPG."""

import json
from game.player import Player

class QuestManager:
    def __init__(self, quests_file: str):
        with open(quests_file, 'r') as f:
            self.quests_db = {q['id']: q for q in json.load(f)}
        self.active_quests: dict[str, dict] = {}
        self.completed_quests: dict[str, dict] = {}

    def start_quest(self, quest_id: str) -> bool:
        if quest_id in self.quests_db and quest_id not in self.active_quests:
            q = json.loads(json.dumps(self.quests_db[quest_id]))
            q['state'] = 'Active'
            self.active_quests[quest_id] = q
            return True
        return False

    def update_objective(self, player: Player, obj_type: str, target_id: str) -> list[str]:
        messages = []
        for q_id, q in list(self.active_quests.items()):
            all_objs_done = True
            for obj in q.get('objectives', []):
                if obj.get('type') == obj_type and obj.get('target') == target_id:
                    if not obj.get('completed'):
                        obj['completed'] = True
                        messages.append(f"Objective Completed: {obj['description']}")

                if not obj.get('completed'):
                    all_objs_done = False

            if all_objs_done and q.get('state') == 'Active':
                q['state'] = 'Completed'
                self.completed_quests[q_id] = q
                del self.active_quests[q_id]
                
                # Award rewards
                rewards = q.get('rewards', {})
                xp = rewards.get('xp', 0)
                credits = rewards.get('credits', 0)
                player.gain_xp(xp)
                player.credits += credits
                messages.append(f"🎉 QUEST COMPLETED: {q['name']}! (+{xp} XP, +{credits} Credits)")

        return messages
