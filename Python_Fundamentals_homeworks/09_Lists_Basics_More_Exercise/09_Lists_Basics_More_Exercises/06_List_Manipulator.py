list_of_number = list(map(int, input().split()))
instruction = input()

while instruction != 'end':
    instruction = instruction.split()
    command = instruction[0]
    if command == 'exchange':
        index = int(instruction[1])
        removed_element = []
        if index >= len(list_of_number) or index < 0:
            print('Invalid index')
        else:
            for digit in range(0, index + 1):
                removed_element.append(list_of_number[digit])
            for element in removed_element:
                list_of_number.remove(element)
            for element in removed_element:
                list_of_number.append(element)

    elif command == 'max':
        max_num = []
        if instruction[1] == 'even':
            for number in list_of_number:
                if number % 2 == 0:
                    max_num.append(number)
        elif instruction[1] == 'odd':
            for number in list_of_number:
                if number % 2 != 0:
                    max_num.append(number)
        if len(max_num) == 0:
            print("No matches")
        else:
            max_number = max(max_num)
            index_of_max_num = 0
            for digit in range(len(list_of_number) - 1, -1, -1):
                if list_of_number[digit] == max_number:
                    index_of_max_num = digit
                    break
            print(index_of_max_num)

    elif command == 'min':
        min_num = []
        if instruction[1] == 'even':
            for number in list_of_number:
                if number % 2 == 0:
                    min_num.append(number)
        elif instruction[1] == 'odd':
            for number in list_of_number:
                if number % 2 != 0:
                    min_num.append(number)
        if len(min_num) == 0:
            print("No matches")
        else:
            min_number = min(min_num)
            index_of_min_num = 0
            for digit in range(len(list_of_number) - 1, -1, -1):
                if list_of_number[digit] == min_number:
                    index_of_min_num = digit
                    break
            print(index_of_min_num)

    elif command == 'first':
        count = int(instruction[1])
        counter = 0
        list_of_count = []
        if count > len(list_of_number):
            print("Invalid count")
        else:
            if instruction[2] == 'even':
                for number in list_of_number:
                    if number % 2 == 0:
                        counter += 1
                        list_of_count.append(number)
                    if counter == count:
                        break
            elif instruction[2] == 'odd':
                for number in list_of_number:
                    if number % 2 != 0:
                        counter += 1
                        list_of_count.append(number)
                    if counter == count:
                        break
            print(list_of_count)

    elif command == 'last':
        count = int(instruction[1])
        counter = 0
        list_of_count = []
        if count > len(list_of_number):
            print("Invalid count")
        else:
            if instruction[2] == 'even':
                for digit in range(len(list_of_number) - 1, -1, -1):
                    current_number = list_of_number[digit]
                    if current_number % 2 == 0:
                        counter += 1
                        list_of_count.append(current_number)
                    if counter == count:
                        break
            elif instruction[2] == 'odd':
                for digit in range(len(list_of_number) - 1, -1, -1):
                    current_number = list_of_number[digit]
                    if current_number % 2 != 0:
                        counter += 1
                        list_of_count.append(current_number)
                    if counter == count:
                        break
            list_of_count.reverse()
            print(list_of_count)

    instruction = input()

print(list_of_number)
