initial_treasure_chest = input().split('|')
instruction = input()

while instruction != 'Yohoho!':
    instruction = instruction.split()
    command = instruction[0]
    if command == 'Loot':
        last_index = len(instruction)
        for item in range(1, last_index):
            item_index = int(item)
            if instruction[item_index] not in initial_treasure_chest:
                initial_treasure_chest.insert(0, instruction[item_index])

    elif command == 'Drop':
        index = int(instruction[1])
        if index in range(len(initial_treasure_chest)):
            remove_loot = initial_treasure_chest[index]
            initial_treasure_chest.remove(remove_loot)
            initial_treasure_chest.append(remove_loot)
    elif command == 'Steal':
        count = int(instruction[1])
        steal_loot = []
        if count <= len(initial_treasure_chest):
            for item_index in range(len(initial_treasure_chest) - count, len(initial_treasure_chest)):
                steal_loot.append(initial_treasure_chest[item_index])
            for steal_item in steal_loot:
                if steal_item in initial_treasure_chest:
                    initial_treasure_chest.remove(str(steal_item))
        else:
            for item_index in range(0, len(initial_treasure_chest)):
                steal_loot.append(initial_treasure_chest[item_index])
            for digit in range(len(initial_treasure_chest) - 1, -1, -1):
                initial_treasure_chest.pop(digit)
        print(', '.join(steal_loot))

    instruction = input()

sum_of_treasure_item = 0
for treasure_item in initial_treasure_chest:
    sum_of_treasure_item += len(treasure_item)

if sum_of_treasure_item > 0:
    average_gain = sum_of_treasure_item / len(initial_treasure_chest)
    print(f"Average treasure gain: {average_gain :.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
