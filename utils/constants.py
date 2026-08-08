"""Game Constants and Enums for Starveil RPG."""

from enum import Enum, auto

class Background(Enum):
    SOLDIER = "Former Soldier"
    SMUGGLER = "Smuggler"
    ENGINEER = "Engineer"
    SCIENTIST = "Scientist"
    CORPORATE = "Corporate Operative"
    BOUNTY_HUNTER = "Bounty Hunter"
    COLONY_SURVIVOR = "Colony Survivor"
    HACKER = "Hacker"
    EXPLORER = "Explorer"

BACKGROUND_BONUSES = {
    Background.SOLDIER: {"strength": 2, "firearms": 3, "health_bonus": 15},
    Background.SMUGGLER: {"agility": 2, "piloting": 3, "stealth": 2},
    Background.ENGINEER: {"technical": 3, "engineering": 4, "energy_bonus": 10},
    Background.SCIENTIST: {"intelligence": 3, "science": 4, "medicine": 2},
    Background.CORPORATE: {"presence": 2, "persuasion": 3, "credits": 300},
    Background.BOUNTY_HUNTER: {"perception": 2, "investigation": 3, "firearms": 2},
    Background.COLONY_SURVIVOR: {"strength": 1, "survival": 4, "health_bonus": 10},
    Background.HACKER: {"technical": 2, "hacking": 4, "intelligence": 1},
    Background.EXPLORER: {"perception": 2, "piloting": 2, "survival": 2}
}

BACKGROUND_DESCRIPTIONS = {
    Background.SOLDIER: "Battle-hardened veteran trained in heavy ordnance and squad tactics.",
    Background.SMUGGLER: "Cunning pilot skilled in bypassing blockade controls and shady deals.",
    Background.ENGINEER: "Tech expert capable of repairing reactors, drives, and structural plating.",
    Background.SCIENTIST: "Researcher knowledgeable in exotic physics, biochemistry, and ancient relics.",
    Background.CORPORATE: "Former executive adept in negotiation, leverage, and corporate politics.",
    Background.BOUNTY_HUNTER: "Relentless tracker specializing in weapon combat and target hunting.",
    Background.COLONY_SURVIVOR: "Resilient survivor of harsh frontier planetary conditions.",
    Background.HACKER: "Cyber-deck specialist who bends electronic security and AI sub-minds to their will.",
    Background.EXPLORER: "Chartist of deep space anomalies, jump gates, and uncharted solar systems."
}

ATTRIBUTE_NAMES = ["strength", "agility", "intelligence", "technical", "presence", "perception"]

SKILL_NAMES = [
    "firearms", "melee", "engineering", "hacking", "medicine",
    "piloting", "persuasion", "intimidation", "stealth", "science",
    "survival", "investigation"
]
