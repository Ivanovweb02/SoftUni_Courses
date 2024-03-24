target_values = list(map(int, input().split()))
instruction = input()

while instruction != 'End':
    instruction = instruction.split()
    command = instruction[0]
    if command == 'Shoot':
        index = int(instruction[1])
        power = int(instruction[2])
        if index in range(len(target_values)):
            target_values[index] -= power
            if target_values[index] <= 0:
                target_values.pop(index)
    elif command == 'Add':
        index = int(instruction[1])
        value = int(instruction[2])
        if index in range(len(target_values)):
            target_values.insert(index, value)
        else:
            print("Invalid placement!")
    elif command == 'Strike':
        index = int(instruction[1])
        radius = int(instruction[2])
        start_index = index - radius
        end_index = index + radius
        if start_index in range(len(target_values)) \
                and end_index in range(len(target_values)):
            for digit in range(end_index, start_index - 1, -1):
                target_values.pop(digit)
        else:
            print('Strike missed!')

    instruction = input()

print(*target_values, sep='|')
