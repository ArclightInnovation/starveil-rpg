"""Spacecraft and interstellar travel engine for Starveil RPG."""

from game.player import Player
from game.world import WorldManager

class TravelManager:
    FUEL_COST_PER_JUMP = 15

    def __init__(self, world_manager: WorldManager):
        self.world_manager = world_manager

    def travel_to_location(self, player: Player, target_location_id: str) -> tuple[bool, str]:
        target_loc = self.world_manager.get_location(target_location_id)
        if not target_loc:
            return False, "Destination location does not exist."

        current_loc = self.world_manager.get_location(player.current_location_id)
        if target_location_id not in current_loc.get('travel_connections', []):
            return False, f"Cannot fly directly from {current_loc.get('name')} to {target_loc.get('name')}."

        if player.ship_fuel < self.FUEL_COST_PER_JUMP:
            return False, f"Insufficient ship fuel! Need {self.FUEL_COST_PER_JUMP} fuel units, but only have {player.ship_fuel}."

        player.ship_fuel -= self.FUEL_COST_PER_JUMP
        player.current_location_id = target_location_id

        return True, f"Jump successful! Consumed {self.FUEL_COST_PER_JUMP} fuel. Arrived at {target_loc['name']} ({target_loc['system']})."
