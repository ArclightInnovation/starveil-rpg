"""Input utilities for Starveil RPG."""

def get_valid_input(prompt_msg: str, valid_choices: list[str]) -> str:
    """Prompts the user until a valid choice is entered."""
    valid_lower = [c.lower() for c in valid_choices]
    while True:
        try:
            choice = input(f"{prompt_msg} ").strip()
            if choice.lower() in valid_lower:
                # Return exact casing from valid choices
                idx = valid_lower.index(choice.lower())
                return valid_choices[idx]
            print(f"Invalid option. Please choose from: {', '.join(valid_choices)}")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting program...")
            exit(0)

def get_int_input(prompt_msg: str, min_val: int, max_val: int) -> int:
    """Prompts for an integer within range."""
    while True:
        try:
            val = int(input(f"{prompt_msg} "))
            if min_val <= val <= max_val:
                return val
            print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid number. Please enter a valid integer.")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting program...")
            exit(0)
