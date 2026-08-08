# Game Design Specification — STARVEIL

## ⚔️ Attributes & Stats
- **Strength (STR):** Health calculation, melee damage, intimidation checks.
- **Agility (AGI):** Evasion, turn order initiative, piloting checks, stealth.
- **Intelligence (INT):** Energy reserve calculation, science, medicine, lore options.
- **Technical (TEC):** Hacking, engineering, energy weapon efficiency.
- **Presence (PRE):** Persuasion, trade prices, companion approval.
- **Perception (PER):** Accuracy, critical hit chance, investigation checks.

## 🎯 Skill System
12 core skills (Firearms, Melee, Engineering, Hacking, Medicine, Piloting, Persuasion, Intimidation, Stealth, Science, Survival, Investigation). Skill checks combine `Skill Level + (Attribute Modifier / 2) + 1d10 Roll >= Difficulty`.

## 🛡️ Combat Mechanics
Turn-based tactical combat featuring:
- **Actions:** Attack, Aim (+20% Accuracy, +15% Crit), Defend, Use Item, Hack, Flee.
- **Armor Mitigation:** Incoming damage reduced directly by armor rating (`Damage = Max(1, RawDamage - Armor)`).
