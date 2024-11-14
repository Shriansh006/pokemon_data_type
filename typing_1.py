type_effectiveness = {
    "normal": {"rock": 0.5, "ghost": 0.0, "steel": 0.5},
    "fire": {"grass": 2.0, "ice": 2.0, "bug": 2.0, "steel": 2.0, "fire": 0.5, "water": 0.5, "rock": 0.5, "dragon": 0.5},
    "water": {"fire": 2.0, "ground": 2.0, "rock": 2.0, "water": 0.5, "grass": 0.5, "dragon": 0.5},
    "electric": {"water": 2.0, "flying": 2.0, "electric": 0.5, "grass": 0.5, "ground": 0.0, "dragon": 0.5},
    "grass": {"water": 2.0, "ground": 2.0, "rock": 2.0, "fire": 0.5, "grass": 0.5, "poison": 0.5, "flying": 0.5, "bug": 0.5, "dragon": 0.5, "steel": 0.5},
    "ice": {"grass": 2.0, "ground": 2.0, "flying": 2.0, "dragon": 2.0, "fire": 0.5, "water": 0.5, "ice": 0.5, "steel": 0.5},
    "fighting": {"normal": 2.0, "ice": 2.0, "rock": 2.0, "dark": 2.0, "steel": 2.0, "poison": 0.5, "flying": 0.5, "psychic": 0.5, "bug": 0.5, "fairy": 0.5, "ghost": 0.0},
    "poison": {"grass": 2.0, "fairy": 2.0, "poison": 0.5, "ground": 0.5, "rock": 0.5, "ghost": 0.5, "steel": 0.0},
    "ground": {"fire": 2.0, "electric": 2.0, "poison": 2.0, "rock": 2.0, "steel": 2.0, "grass": 0.5, "bug": 0.5, "flying": 0.0},
    "flying": {"grass": 2.0, "fighting": 2.0, "bug": 2.0, "electric": 0.5, "rock": 0.5, "steel": 0.5},
    "psychic": {"fighting": 2.0, "poison": 2.0, "psychic": 0.5, "steel": 0.5, "dark": 0.0},
    "bug": {"grass": 2.0, "psychic": 2.0, "dark": 2.0, "fire": 0.5, "fighting": 0.5, "poison": 0.5, "flying": 0.5, "ghost": 0.5, "steel": 0.5, "fairy": 0.5},
    "rock": {"fire": 2.0, "ice": 2.0, "flying": 2.0, "bug": 2.0, "fighting": 0.5, "ground": 0.5, "steel": 0.5},
    "ghost": {"psychic": 2.0, "ghost": 2.0, "normal": 0.0, "dark": 0.5},
    "dragon": {"dragon": 2.0, "steel": 0.5, "fairy": 0.0},
    "dark": {"psychic": 2.0, "ghost": 2.0, "fighting": 0.5, "dark": 0.5, "fairy": 0.5},
    "steel": {"ice": 2.0, "rock": 2.0, "fairy": 2.0, "fire": 0.5, "water": 0.5, "electric": 0.5, "steel": 0.5},
    "fairy": {"fighting": 2.0, "dragon": 2.0, "dark": 2.0, "fire": 0.5, "poison": 0.5, "steel": 0.5}
}

attacker_type=input("Attacking move type: ").strip().lower()
target_type1=input("Target's first type: ").strip().lower()
target_type2=input("Target's Second Type (or leave blank if none): ").strip().lower() or None
base_damage = float(input("Base Damage: "))


if attacker_type not in type_effectiveness:
    print(f"Error: '{attacker_type}' is not a valid attacker type.")
elif target_type1 not in type_effectiveness.get(attacker_type, {}) and target_type1 != "":
    print(f"Error: '{target_type1}' is not a valid target type for effectiveness calculation.")
elif target_type2 and target_type2 not in type_effectiveness.get(attacker_type, {}):
    print(f"Error: '{target_type2}' is not a valid target type for effectiveness calculation.")
else:
  multiplier1 = type_effectiveness.get(attacker_type, {}).get(target_type1, 1.0)
  multiplier2 = type_effectiveness.get(attacker_type, {}).get(target_type2, 1.0) if target_type2 else 1.0
  final_damage = base_damage * multiplier1 * multiplier2
  print(f"Final Damage: {final_damage}")
