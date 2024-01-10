pokemon_distance = list(map(int, input().split()))
removed_element = []

while len(pokemon_distance) != 0:
    index = int(input())
    current_remove_element = 0
    if index in range(len(pokemon_distance)):
        removed_element.append(pokemon_distance[index])
        current_remove_element = pokemon_distance[index]
        pokemon_distance.pop(index)
        for digit in range(len(pokemon_distance)):
            current_index = digit
            if pokemon_distance[current_index] > current_remove_element:
                pokemon_distance[current_index] -= current_remove_element
            else:
                pokemon_distance[current_index] += current_remove_element

    elif index < 0:
        current_remove_element = pokemon_distance[0]
        removed_element.append(pokemon_distance[0])
        pokemon_distance[0] = pokemon_distance[-1]
        for digit in range(len(pokemon_distance)):
            current_index = digit
            if pokemon_distance[current_index] > current_remove_element:
                pokemon_distance[current_index] -= current_remove_element
            else:
                pokemon_distance[current_index] += current_remove_element

    elif index > len(pokemon_distance) - 1:
        current_remove_element = pokemon_distance[-1]
        removed_element.append(pokemon_distance[-1])
        pokemon_distance[-1] = pokemon_distance[0]
        for digit in range(len(pokemon_distance)):
            current_index = digit
            if pokemon_distance[current_index] > current_remove_element:
                pokemon_distance[current_index] -= current_remove_element
            else:
                pokemon_distance[current_index] += current_remove_element

print(sum(removed_element))
