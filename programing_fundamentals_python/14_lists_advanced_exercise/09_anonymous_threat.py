data = input().split()
instruction = input()

while instruction != '3:1':
    instruction = instruction.split()
    command = instruction[0]
    if command == 'merge':
        start_index = int(instruction[1])
        end_index = int(instruction[2])
        if start_index < 0:
            start_index = 0
        if end_index > len(data) - 1:
            end_index = len(data) - 1
        for current_index, string in enumerate(data):
            if current_index in range(start_index + 1, end_index + 1):
                data[start_index] += data[current_index]
        for current_index in range(end_index, start_index, -1):
            data.pop(current_index)
    elif command == 'divide':
        index = int(instruction[1])
        partitions = int(instruction[2])
        if partitions > len(data[index]):
            steps = 1
        else:
            steps = len(data[index]) // partitions
        divided_part = data.pop(index)
        start = 0
        for parts in range(partitions):
            if parts == partitions - 1:
                data.insert(index, divided_part[start::])
                break
            else:
                data.insert(index, divided_part[start: start + steps])
            start += steps
            index += 1

    instruction = input()

print(' '.join(data))
