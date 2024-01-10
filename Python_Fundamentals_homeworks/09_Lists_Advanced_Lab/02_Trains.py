wagon = [0] * int(input())

while True:
    command = input().split()
    if command[0] == 'End':
        break
    if 'add' in command:
        count_of_people = int(command[1])
        wagon[-1] += count_of_people
    elif 'insert' in command:
        index = int(command[1])
        count_of_people = int(command[2])
        wagon[index] += count_of_people
    elif 'leave' in command:
        index = int(command[1])
        count_of_people = int(command[2])
        wagon[index] -= count_of_people

print(wagon)
