sequence_of_element = input().split()
instruction = input()
movie_count = 0

are_elements_hit = False
while instruction != 'end':
    movie_count += 1
    instruction = instruction.split()
    index_1 = int(instruction[0])
    index_2 = int(instruction[1])
    if (index_1 == index_2) \
            or index_1 not in range(len(sequence_of_element)) \
            or index_2 not in range(len(sequence_of_element)):
        bonus_element = f"-{movie_count}a"
        bonus_index = len(sequence_of_element) // 2
        sequence_of_element.insert(bonus_index, bonus_element)
        sequence_of_element.insert(bonus_index, bonus_element)
        print("Invalid input! Adding additional elements to the board")
    else:
        if sequence_of_element[index_1] == sequence_of_element[index_2]:
            element = sequence_of_element[index_1]
            for _ in range(len(sequence_of_element)):
                if element in sequence_of_element:
                    sequence_of_element.remove(element)
            print(f"Congrats! You have found matching elements - {element}!")
        elif sequence_of_element[index_1] != sequence_of_element[index_2]:
            print("Try again!")

    if len(sequence_of_element) == 0:
        are_elements_hit = True
        break

    instruction = input()

if are_elements_hit:
    print(f"You have won in {movie_count} turns!")
else:
    result = ' '.join(sequence_of_element)
    print(f"Sorry you lose :(\n"
          f"{result}")
