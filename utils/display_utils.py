"""Display utilities for terminal formatting in Starveil RPG."""

LINE_WIDTH = 70

def print_header(title: str):
    print("\n" + "=" * LINE_WIDTH)
    print(f" {title.upper().center(LINE_WIDTH - 2)} ")
    print("=" * LINE_WIDTH)

def print_subheader(title: str):
    print("\n" + "-" * LINE_WIDTH)
    print(f" {title.center(LINE_WIDTH - 2)} ")
    print("-" * LINE_WIDTH)

def print_box(text: str):
    lines = text.split("\n")
    print("┌" + "─" * (LINE_WIDTH - 2) + "┐")
    for line in lines:
        print(f"│ {line.ljust(LINE_WIDTH - 4)} │")
    print("└" + "─" * (LINE_WIDTH - 2) + "┘")

def print_menu(options: list[str]):
    for idx, opt in enumerate(options, 1):
        print(f" [{idx}] {opt}")
    print()
