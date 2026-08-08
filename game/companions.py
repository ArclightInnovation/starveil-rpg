"""Recruitable companions for Starveil RPG."""

from dataclasses import dataclass, field

@dataclass
class Companion:
    id: str
    name: str
    background: str
    personality: str
    faction_affiliation: str
    relationship_score: int = 50
    is_recruited: bool = False

COMPANIONS_DATABASE = {
    "vex": Companion(
        id="vex",
        name="Vex",
        background="Ex-Syndicate Infiltrator",
        personality="Cynical, sharp-witted, fiercely loyal once earned.",
        faction_affiliation="vaelen_syndicate"
    ),
    "dr_maya_lin": Companion(
        id="dr_maya_lin",
        name="Dr. Maya Lin",
        background="Aegis Xenobiologist",
        personality="Analytical, empathetic, obsessed with ancient AI relics.",
        faction_affiliation="aegis_corp"
    ),
    "commander_jax": Companion(
        id="commander_jax",
        name="Commander Jax",
        background="Free Colonies Veteran",
        personality="Disciplined, stoic, devoted to frontier liberty.",
        faction_affiliation="free_colonies"
    )
}
