"""Character attributes and stats calculation for Starveil RPG."""

from dataclasses import dataclass, field
from utils.constants import ATTRIBUTE_NAMES, SKILL_NAMES

@dataclass
class Attributes:
    strength: int = 5
    agility: int = 5
    intelligence: int = 5
    technical: int = 5
    presence: int = 5
    perception: int = 5

    def get_attr(self, name: str) -> int:
        return getattr(self, name.lower(), 5)

    def set_attr(self, name: str, value: int):
        setattr(self, name.lower(), value)

@dataclass
class Skills:
    firearms: int = 1
    melee: int = 1
    engineering: int = 1
    hacking: int = 1
    medicine: int = 1
    piloting: int = 1
    persuasion: int = 1
    intimidation: int = 1
    stealth: int = 1
    science: int = 1
    survival: int = 1
    investigation: int = 1

    def get_skill(self, name: str) -> int:
        return getattr(self, name.lower(), 0)

    def set_skill(self, name: str, value: int):
        setattr(self, name.lower(), value)

@dataclass
class DerivedStats:
    health: int = 100
    max_health: int = 100
    energy: int = 50
    max_energy: int = 50
    armor: int = 0
    accuracy: int = 75
    critical_chance: int = 5
    evasion: int = 5

    def recalculate(self, attributes: Attributes, bonus_health: int = 0, bonus_energy: int = 0):
        self.max_health = 80 + (attributes.strength * 10) + bonus_health
        self.max_energy = 40 + (attributes.technical * 5) + (attributes.intelligence * 5) + bonus_energy
        self.accuracy = 70 + (attributes.perception * 3) + (attributes.agility * 2)
        self.critical_chance = 3 + (attributes.perception * 2)
        self.evasion = 3 + (attributes.agility * 2)
        
        if self.health > self.max_health:
            self.health = self.max_health
        if self.energy > self.max_energy:
            self.energy = self.max_energy
