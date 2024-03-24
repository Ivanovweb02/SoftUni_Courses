list_of_groceries = input().split('!')
instruction = input()

while instruction != 'Go Shopping!':
    instruction = instruction.split()
    command = instruction[0]
    item = instruction[1]
    if command == 'Urgent':
        if item not in list_of_groceries:
            list_of_groceries.insert(0, item)
    elif item in list_of_groceries:
        if command == 'Unnecessary':
            list_of_groceries.remove(item)
        elif command == 'Correct':
            new_item = instruction[2]
            index = list_of_groceries.index(item)
            list_of_groceries[index] = new_item
        elif command == 'Rearrange':
            list_of_groceries.remove(item)
            list_of_groceries.append(item)

    instruction = input()

print(", ".join(list_of_groceries))
