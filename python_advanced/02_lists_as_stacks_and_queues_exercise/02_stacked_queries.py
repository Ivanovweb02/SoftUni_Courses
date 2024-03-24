lines = int(input())
list_of_numbers = []

for _ in range(lines):
    command = input().split()
    instruction = command[0]
    if instruction == '1':
        number = int(command[1])
        list_of_numbers.append(number)
    elif list_of_numbers:
        if instruction == '2':
            list_of_numbers.pop()
        elif instruction == '3':
            print(max(list_of_numbers))
        elif instruction == '4':
            print(min(list_of_numbers))

result = reversed([str(number) for number in list_of_numbers])
print(', '.join(result))
