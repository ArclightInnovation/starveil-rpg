# ✦ STARVEIL: SHADOWS OF THE SECTOR

An original, modular, text-based Science-Fiction RPG & AI Game Master built with Python and HTML5/Web Terminal capabilities.

---

## 🚀 Overview

Hundreds of years in the future, humanity has scattered across fragmented star systems ruled by megacorporations, independent colony coalitions, rogue synthetics, and criminal syndicates. You play as an operative drawn into a dark cosmic mystery surrounding an ancient alien transmission and a rogue AI sub-mind.

### 🎮 Features
- **Flexible RPG Engine:** 6 Core Attributes, 12 Skills, Derived Combat Stats, XP & Leveling.
- **Backgrounds:** 9 Player Backgrounds affecting stats, starting equipment, dialogue checks, and faction relationships.
- **Data-Driven Architecture:** Items, weapons, enemies, locations, dialogue trees, encounters, and quests loaded from JSON.
- **Turn-Based Combat:** Tactical combat with aim, defend, item usage, hacking, armor mitigation, and AI decision-making.
- **Interstellar Travel:** Jump navigation between star systems, ship fuel/hull management, and random space interdictions.
- **Gemini AI Game Master:** Integrated Google Gemini API support for dynamic, real-time ambient narration & NPC dialogue generation.
- **Dual Play Modes:** Play directly via Python terminal (`python main.py`) OR in the browser via GitHub Pages.

---

## 💻 Installation & How to Run

### **Option 1: Play in Browser (Web App / GitHub Pages)**
Visit the deployed web application:
🔗 **[STARVEIL Live Web App](https://arclightinnovation.github.io/starveil-rpg/)**

### **Option 2: Run Terminal CLI Locally (Python 3.12+)**

1. **Clone Repository:**
   ```bash
   git clone https://github.com/ArclightInnovation/starveil-rpg.git
   cd starveil-rpg
   ```

2. **Run Game:**
   ```bash
   python main.py
   ```

3. **Run Automated Tests:**
   ```bash
   python tests/test_character.py
   python tests/test_combat.py
   python tests/test_save.py
   ```

---

## 🔑 Gemini API Key Configuration
To enable dynamic AI Game Master narration:
- **In Web App:** Click `🔑 Gemini API Key` in the top header and paste your key. It is saved strictly in your browser's `localStorage` and never transmitted to external servers.
- **In Python CLI:** Set `export GEMINI_API_KEY="your_api_key_here"` before running `python main.py`.

---

## 📜 Documentation
- [`ARCHITECTURE.md`](ARCHITECTURE.md) — System architecture & decoupling
- [`GAME_DESIGN.md`](GAME_DESIGN.md) — Stats, skills, combat, progression rules
- [`LORE.md`](LORE.md) — Universe lore, factions, and story acts
- [`DEVLOG.md`](DEVLOG.md) — Implementation devlog
