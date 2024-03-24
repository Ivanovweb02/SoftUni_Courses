array_of_numbers = list(map(int, input().split()))
instruction = input()

while instruction != 'end':
    instruction = instruction.split()
    command = instruction[0]
    if command == 'swap':
        index_1 = int(instruction[1])
        index_2 = int(instruction[2])
        array_of_numbers[index_1], array_of_numbers[index_2] = array_of_numbers[index_2], array_of_numbers[index_1]
    elif command == 'multiply':
        index_1 = int(instruction[1])
        index_2 = int(instruction[2])
        array_of_numbers[index_1] *= array_of_numbers[index_2]
    elif command == 'decrease':
        for index in range(len(array_of_numbers)):
            array_of_numbers[index] -= 1
    instruction = input()

# print(', '.join(map(str, array_of_numbers)))
for current_index in range(len(array_of_numbers)):
    output = array_of_numbers[current_index]
    if current_index == (len(array_of_numbers) - 1):
        print(output)
    else:
        print(output, end=', ')
