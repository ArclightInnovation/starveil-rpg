"""Player character model and progression system for Starveil RPG."""

from dataclasses import dataclass, field
from game.character import Attributes, Skills, DerivedStats
from utils.constants import Background, BACKGROUND_BONUSES, BACKGROUND_DESCRIPTIONS

@dataclass
class Player:
    name: str = "Unknown Traveler"
    background: str = Background.SOLDIER.value
    level: int = 1
    xp: int = 0
    xp_to_next_level: int = 100
    stat_points: int = 0
    skill_points: int = 0
    credits: int = 500
    
    attributes: Attributes = field(default_factory=Attributes)
    skills: Skills = field(default_factory=Skills)
    derived: DerivedStats = field(default_factory=DerivedStats)
    
    perks: list[str] = field(default_factory=list)
    inventory_items: list[dict] = field(default_factory=list)
    equipped_weapon: dict = field(default_factory=dict)
    equipped_armor: dict = field(default_factory=dict)
    equipped_tech: dict = field(default_factory=dict)

    current_location_id: str = "station_khepri"
    current_ship_name: str = "SS Starseeker"
    ship_hull: int = 100
    ship_max_hull: int = 100
    ship_fuel: int = 50
    ship_max_fuel: int = 100

    def apply_background(self):
        bg_enum = None
        for b in Background:
            if b.value == self.background:
                bg_enum = b
                break
        
        bonus_hp = 0
        bonus_ep = 0

        if bg_enum and bg_enum in BACKGROUND_BONUSES:
            bonuses = BACKGROUND_BONUSES[bg_enum]
            for stat, val in bonuses.items():
                if stat in ["strength", "agility", "intelligence", "technical", "presence", "perception"]:
                    cur = self.attributes.get_attr(stat)
                    self.attributes.set_attr(stat, cur + val)
                elif stat in ["firearms", "melee", "engineering", "hacking", "medicine", "piloting", "persuasion", "intimidation", "stealth", "science", "survival", "investigation"]:
                    cur = self.skills.get_skill(stat)
                    self.skills.set_skill(stat, cur + val)
                elif stat == "credits":
                    self.credits += val
                elif stat == "health_bonus":
                    bonus_hp += val
                elif stat == "energy_bonus":
                    bonus_ep += val

        self.derived.recalculate(self.attributes, bonus_health=bonus_hp, bonus_energy=bonus_ep)
        self.derived.health = self.derived.max_health
        self.derived.energy = self.derived.max_energy

    def gain_xp(self, amount: int) -> bool:
        """Gains XP and handles leveling up. Returns True if leveled up."""
        self.xp += amount
        leveled_up = False
        while self.xp >= self.xp_to_next_level:
            self.xp -= self.xp_to_next_level
            self.level += 1
            self.xp_to_next_level = int(self.xp_to_next_level * 1.5)
            self.stat_points += 2
            self.skill_points += 3
            leveled_up = True

        if leveled_up:
            self.derived.recalculate(self.attributes)
            self.derived.health = self.derived.max_health
            self.derived.energy = self.derived.max_energy
        return leveled_up

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "background": self.background,
            "level": self.level,
            "xp": self.xp,
            "xp_to_next_level": self.xp_to_next_level,
            "stat_points": self.stat_points,
            "skill_points": self.skill_points,
            "credits": self.credits,
            "attributes": {
                "strength": self.attributes.strength,
                "agility": self.attributes.agility,
                "intelligence": self.attributes.intelligence,
                "technical": self.attributes.technical,
                "presence": self.attributes.presence,
                "perception": self.attributes.perception
            },
            "skills": {k: self.skills.get_skill(k) for k in [
                "firearms", "melee", "engineering", "hacking", "medicine",
                "piloting", "persuasion", "intimidation", "stealth", "science",
                "survival", "investigation"
            ]},
            "health": self.derived.health,
            "energy": self.derived.energy,
            "perks": self.perks,
            "inventory_items": self.inventory_items,
            "equipped_weapon": self.equipped_weapon,
            "equipped_armor": self.equipped_armor,
            "equipped_tech": self.equipped_tech,
            "current_location_id": self.current_location_id,
            "current_ship_name": self.current_ship_name,
            "ship_hull": self.ship_hull,
            "ship_fuel": self.ship_fuel
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Player":
        p = cls(
            name=data.get("name", "Traveler"),
            background=data.get("background", Background.SOLDIER.value),
            level=data.get("level", 1),
            xp=data.get("xp", 0),
            xp_to_next_level=data.get("xp_to_next_level", 100),
            stat_points=data.get("stat_points", 0),
            skill_points=data.get("skill_points", 0),
            credits=data.get("credits", 500),
            perks=data.get("perks", []),
            inventory_items=data.get("inventory_items", []),
            equipped_weapon=data.get("equipped_weapon", {}),
            equipped_armor=data.get("equipped_armor", {}),
            equipped_tech=data.get("equipped_tech", {}),
            current_location_id=data.get("current_location_id", "station_khepri"),
            current_ship_name=data.get("current_ship_name", "SS Starseeker"),
            ship_hull=data.get("ship_hull", 100),
            ship_fuel=data.get("ship_fuel", 50)
        )
        attrs = data.get("attributes", {})
        for k, v in attrs.items():
            p.attributes.set_attr(k, v)

        sk = data.get("skills", {})
        for k, v in sk.items():
            p.skills.set_skill(k, v)

        p.derived.recalculate(p.attributes)
        p.derived.health = data.get("health", p.derived.max_health)
        p.derived.energy = data.get("energy", p.derived.max_energy)
        return p
