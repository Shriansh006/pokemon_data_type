
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


nature = input("Nature: ").strip().lower()


if nature in nature_effects:
    for effect in nature_effects[nature]:
        print(effect)
else:
    print("This nature does not exist :(")
