"""STARVEIL: SHADOWS OF THE SECTOR
Main CLI Entry Point.
"""

import sys
import os

# Ensure game directory is on path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from game.game import GameEngine
from utils.constants import Background, BACKGROUND_DESCRIPTIONS
from utils.display_utils import print_header, print_subheader, print_box, print_menu
from utils.input_utils import get_valid_input, get_int_input

def character_creation(engine: GameEngine):
    print_header("Character Creation")
    name = input("Enter your character name: ").strip()
    if not name:
        name = "Kaelen Vance"

    print("\nSelect your character background:")
    bgs = [b.value for b in Background]
    for idx, b in enumerate(bgs, 1):
        desc = BACKGROUND_DESCRIPTIONS.get(Background(b), "")
        print(f" [{idx}] {b.ljust(22)} - {desc}")

    choice_idx = get_int_input("Choose background (1-9):", 1, len(bgs))
    selected_bg = bgs[choice_idx - 1]

    player = engine.create_character(name, selected_bg)
    print_box(f"Welcome, {player.name}!\nBackground: {player.background}\nStarting Credits: {player.credits} CR\nHealth: {player.derived.health}/{player.derived.max_health} HP")

def main_game_loop(engine: GameEngine):
    while True:
        loc = engine.get_current_location_data()
        print_header(f"{loc.get('name', 'Unknown Region')} ({loc.get('system', '')})")
        print(loc.get('description', ''))
        
        # Narration
        narrative = engine.trigger_location_narration()
        print(f"\n{narrative}\n")

        print("ACTIONS:")
        print(" [1] Explore Location Sub-Areas")
        print(" [2] Speak with NPCs")
        print(" [3] Open Starship Navigation & Interstellar Travel")
        print(" [4] Check Quest Journal")
        print(" [5] Character Sheet & Inventory")
        print(" [6] Save Game")
        print(" [7] Exit Game")

        choice = get_int_input("Select action (1-7):", 1, 7)

        if choice == 1:
            sub = loc.get('sub_locations', [])
            print_subheader("Sub-Locations")
            for idx, s in enumerate(sub, 1):
                print(f" [{idx}] {s}")
            print(f" [{len(sub) + 1}] Return")
            s_choice = get_int_input("Select area:", 1, len(sub) + 1)
            if s_choice <= len(sub):
                area_name = sub[s_choice - 1]
                print_box(f"You explore {area_name}. The area is quiet with humming power conduits.")

        elif choice == 2:
            npcs = loc.get('npcs', [])
            if not npcs:
                print("\nNo active NPCs found in this area.")
                continue
            print_subheader("Available NPCs")
            for idx, npc in enumerate(npcs, 1):
                print(f" [{idx}] {npc.replace('_', ' ').title()}")
            print(f" [{len(npcs) + 1}] Return")
            n_choice = get_int_input("Speak with:", 1, len(npcs) + 1)
            if n_choice <= len(npcs):
                npc_id = npcs[n_choice - 1]
                run_dialogue(engine, npc_id)

        elif choice == 3:
            print_subheader("Interstellar Travel Navigation")
            dests = engine.world_mgr.get_available_travel_destinations(engine.player.current_location_id)
            print(f"Current Ship: {engine.player.current_ship_name} | Fuel: {engine.player.ship_fuel}/{engine.player.ship_max_fuel}")
            for idx, d in enumerate(dests, 1):
                print(f" [{idx}] {d['name']} ({d['system']}) - Fuel Cost: {engine.travel_mgr.FUEL_COST_PER_JUMP}")
            print(f" [{len(dests) + 1}] Return")
            t_choice = get_int_input("Jump to:", 1, len(dests) + 1)
            if t_choice <= len(dests):
                target = dests[t_choice - 1]
                ok, msg = engine.travel_mgr.travel_to_location(engine.player, target['id'])
                print(f"\n{msg}")

        elif choice == 4:
            print_subheader("Quest Journal")
            if not engine.quest_mgr.active_quests:
                print("No active quests.")
            for q_id, q in engine.quest_mgr.active_quests.items():
                print(f"• {q['name']} ({q['type'].upper()})")
                print(f"  Description: {q['description']}")
                for obj in q['objectives']:
                    status = "✓" if obj['completed'] else "○"
                    print(f"  [{status}] {obj['description']}")

        elif choice == 5:
            print_subheader("Character Sheet & Inventory")
            p = engine.player
            print(f"Name: {p.name} | Level: {p.level} (XP: {p.xp}/{p.xp_to_next_level})")
            print(f"HP: {p.derived.health}/{p.derived.max_health} | Energy: {p.derived.energy}/{p.derived.max_energy} | Credits: {p.credits} CR")
            print(f"Attributes: STR {p.attributes.strength} | AGI {p.attributes.agility} | INT {p.attributes.intelligence} | TEC {p.attributes.technical} | PRE {p.attributes.presence} | PER {p.attributes.perception}")
            print(f"Equipped Weapon: {p.equipped_weapon.get('name', 'None')}")
            print(f"Equipped Armor: {p.equipped_armor.get('name', 'None')}")
            print("\nInventory Items:")
            for idx, item in enumerate(p.inventory_items, 1):
                print(f"  [{idx}] {item['name']} ({item['type'].capitalize()}) - {item.get('description', '')}")

        elif choice == 6:
            if engine.save_game_state():
                print("\n✅ Game state saved successfully!")
            else:
                print("\n❌ Save failed.")

        elif choice == 7:
            print("\nThank you for playing STARVEIL! Goodbye.")
            break

def run_dialogue(engine: GameEngine, npc_id: str):
    curr_node = "start"
    while True:
        node = engine.dialogue_mgr.get_node(npc_id, curr_node)
        if not node:
            break
        print_subheader(f"Dialogue: {npc_id.replace('_', ' ').title()}")
        print(f"\"{node.get('npc_text')}\"\n")

        opts = engine.dialogue_mgr.evaluate_options(engine.player, node.get('options', []))
        if not opts:
            break

        for idx, opt in enumerate(opts, 1):
            print(f" [{idx}] {opt['text']}")

        choice = get_int_input("Choose response:", 1, len(opts))
        selected = opts[choice - 1]

        # Trigger actions
        if selected.get('action') == 'start_quest_act1':
            engine.quest_mgr.start_quest('quest_act1_main')
            print("\n📜 Quest Started: Act I: Signal in the Dark!")

        if 'skill_check' in selected:
            sc = selected['skill_check']
            from game.skill_checks import SkillCheckSystem
            success, msg = SkillCheckSystem.perform_check(engine.player, sc['skill'], sc['difficulty'])
            print(f"\n{msg}")
            if success:
                curr_node = selected.get('success_next', 'node_end')
            else:
                curr_node = selected.get('failure_next', 'node_end')
        else:
            curr_node = selected.get('next', 'node_end')

if __name__ == "__main__":
    engine = GameEngine()
    character_creation(engine)
    main_game_loop(engine)
