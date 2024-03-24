pokemon_distance = list(map(int, input().split()))
list_removed_pokemon = []

while len(pokemon_distance) != 0:
    index = int(input())
    removed_pokemon = 0
    if index in range(len(pokemon_distance)):
        removed_pokemon = pokemon_distance[index]
        list_removed_pokemon.append(removed_pokemon)
        pokemon_distance.pop(index)

    elif index < 0:
        index = 0
        copied_pokemon = pokemon_distance[-1]
        removed_pokemon = pokemon_distance[index]
        list_removed_pokemon.append(removed_pokemon)
        pokemon_distance.pop(index)
        pokemon_distance.insert(index, copied_pokemon)

    else:
        index = (len(pokemon_distance) - 1)
        copied_pokemon = pokemon_distance[0]
        removed_pokemon = pokemon_distance[index]
        list_removed_pokemon.append(removed_pokemon)
        pokemon_distance.pop(index)
        pokemon_distance.insert(index, copied_pokemon)

    for pokemon_digit in range(len(pokemon_distance)):
        if removed_pokemon >= pokemon_distance[pokemon_digit]:
            pokemon_distance[pokemon_digit] += removed_pokemon
        else:
            pokemon_distance[pokemon_digit] -= removed_pokemon

print(sum(list_removed_pokemon))
