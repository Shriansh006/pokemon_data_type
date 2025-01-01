def display_all_natures(nature_effects):
    """Displays all available natures and their effects."""
    print("\nAvailable Natures and Their Effects:\n")
    for nature, effects in nature_effects.items():
        effects_str = " | ".join(effects)
        print(f"{nature.capitalize()}: {effects_str}")


def get_nature_effect(nature, nature_effects):
    """Gets the effects of a specific nature."""
    return nature_effects.get(nature, ("This nature does not exist :("))



nature_effects = {
    "adamant": ("Attack stats increases", "Sp.Attack stats decreases"),
    "bold": ("Defense stats increases", "Attack stats decreases"),
    "brave": ("Attack stats increases", "Speed stats decreases"),
    "calm": ("Sp.Defense stats increases", "Attack stats decreases"),
    "careful": ("Sp.Defense stats increases", "Sp.Attack stats decreases"),
    "gentle": ("Sp.Defense stats increases", "Defense stats decreases"),
    "hasty": ("Speed stats increases", "Defense stats decreases"),
    "impish": ("Defense stats increases", "Sp.Attack stats decreases"),
    "jolly": ("Speed stats increases", "Sp.Attack stats decreases"),
    "lax": ("Defense stats increases", "Sp.Defense stats decreases"),
    "lonely": ("Attack stats increases", "Defense stats decreases"),
    "mild": ("Sp.Attack stats increases", "Defense stats decreases"),
    "naive": ("Speed stats increases", "Sp.Defense stats decreases"),
    "naughty": ("Attack stats increases", "Sp.Defense stats decreases"),
    "quiet": ("Sp.Attack stats increases", "Speed stats decreases"),
    "rash": ("Sp.Attack stats increases", "Sp.Defense stats decreases"),
    "relaxed": ("Defense stats increases", "Speed stats decreases"),
    "sassy": ("Sp.Defense stats increases", "Speed stats decreases"),
    "timid": ("Speed stats increases", "Attack stats decreases"),
    "bashful": ("This pokemon is neutral in nature",),
    "docile": ("This pokemon is neutral in nature",),
    "hardy": ("This pokemon is neutral in nature",),
    "quirky": ("This pokemon is neutral in nature",),
    "serious": ("This pokemon is neutral in nature",)
}

while True:
    print("\nMenu:")
    print("1. View nature effects")
    print("2. View all natures")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        nature = input("Enter a nature: ").strip().lower()
        effects = get_nature_effect(nature, nature_effects)
        for effect in effects:
            print(effect)
    elif choice == "2":
        display_all_natures(nature_effects)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
