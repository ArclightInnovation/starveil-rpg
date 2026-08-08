"""World, systems, and location management for Starveil RPG."""

import json

class WorldManager:
    def __init__(self, locations_file: str):
        with open(locations_file, 'r') as f:
            self.locations = {loc['id']: loc for loc in json.load(f)}

    def get_location(self, location_id: str) -> dict:
        return self.locations.get(location_id, {})

    def get_available_travel_destinations(self, current_location_id: str) -> list[dict]:
        current_loc = self.get_location(current_location_id)
        connections = current_loc.get('travel_connections', [])
        return [self.get_location(cid) for cid in connections if cid in self.locations]
