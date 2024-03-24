from collections import deque

quantity_of_water = int(input())
people = deque()

name = input()
while name != 'Start':
    people.append(name)
    name = input()

instruction = input()
while instruction != 'End':
    instruction = instruction.split()
    command = instruction[0]
    if command.isdigit():
        liters = int(command)
        person_name = people.popleft()
        if quantity_of_water >= liters:
            quantity_of_water -= liters
            print(f"{person_name} got water")
        else:
            print(f"{person_name} must wait")
    elif command == 'refill':
        liters = int(instruction[1])
        quantity_of_water += liters

    instruction = input()
print(f"{quantity_of_water} liters left")
