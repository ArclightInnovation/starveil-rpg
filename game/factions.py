"""Faction reputation system for Starveil RPG."""

import json

class FactionSystem:
    def __init__(self, factions_file: str):
        with open(factions_file, 'r') as f:
            self.factions = {fac['id']: fac for fac in json.load(f)}

    def modify_reputation(self, faction_id: str, delta: int) -> str:
        if faction_id in self.factions:
            self.factions[faction_id]['reputation'] += delta
            rep = self.factions[faction_id]['reputation']
            status = "Neutral"
            if rep >= 50:
                status = "Honored"
            elif rep >= 25:
                status = "Friendly"
            elif rep <= -50:
                status = "Hostile"
            elif rep <= -25:
                status = "Unfriendly"
            return f"Reputation with {self.factions[faction_id]['name']} changed by {delta:+d} (Current: {rep} - {status})"
        return f"Unknown faction: {faction_id}"

    def get_reputation_status(self, faction_id: str) -> str:
        if faction_id in self.factions:
            rep = self.factions[faction_id]['reputation']
            if rep >= 50: return "Honored"
            if rep >= 25: return "Friendly"
            if rep <= -25: return "Unfriendly"
            if rep <= -50: return "Hostile"
            return "Neutral"
        return "Unknown"
