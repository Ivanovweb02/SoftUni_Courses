activation_key = input()
instruction = input()

while instruction != 'Generate':
    instruction = instruction.split('>>>')
    command = instruction[0]
    if command == 'Contains':
        substring = instruction[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif command == 'Flip':
        upper_lower = instruction[1]
        start_index = int(instruction[2])
        end_index = int(instruction[3])
        if upper_lower == 'Upper':
            activation_key = activation_key[0:start_index] + activation_key[start_index:end_index].upper() \
                             + activation_key[end_index: len(activation_key) + 1]
        elif upper_lower == 'Lower':
            activation_key =  activation_key[0:start_index] + activation_key[start_index:end_index].lower() \
                              + activation_key[end_index: len(activation_key) + 1]
        print(activation_key)

    elif command == 'Slice':
        start_index = int(instruction[1])
        end_index = int(instruction[2])
        for index in range(end_index - 1, start_index - 1, - 1):
            activation_key = activation_key.replace(activation_key[index], "", 1)
        print(activation_key)

    instruction = input()
print(f"Your activation key is: {activation_key}")
