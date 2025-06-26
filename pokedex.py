import pokebase as pb


pokemon_name = input("Enter a Pokémon name: ").lower()


try:
    pokemon = pb.pokemon(pokemon_name)

    print(f"\nName       : {pokemon.name.capitalize()}")
    print(f"ID         : {pokemon.id}")
    print("Stats      :")
    for stats in pokemon.stats:
        print(f" - {stats.stat.name}: {stats.base_stat}")
    print("Abilities  :")
    for ability in pokemon.abilities:
        print(f" - {ability.ability.name}")
    print("Types      :")
    for poke_type in pokemon.types:
        print(f" - {poke_type.type.name}")

except Exception as e:
    print("Could not fetch Pokémon. Please check the name.")
