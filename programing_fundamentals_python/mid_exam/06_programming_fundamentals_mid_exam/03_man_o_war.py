def fire():
    index = int(instruction[1])
    damage = int(instruction[2])
    if index in range(len(warship_status)):
        warship_status[index] -= damage
        if warship_status[index] <= 0:
            return True


def defend():
    start_index = int(instruction[1])
    end_index = int(instruction[2])
    damage = int(instruction[3])
    if start_index in range(len(pirate_ship_status)) \
            and end_index in range(len(pirate_ship_status)):
        for index in range(start_index, end_index + 1):
            pirate_ship_status[index] -= damage
            if pirate_ship_status[index] <= 0:
                return True


def repair():
    index = int(instruction[1])
    health = int(instruction[2])
    if index in range(len(pirate_ship_status)):
        pirate_ship_status[index] += health
        if pirate_ship_status[index] > max_health_capacity:
            pirate_ship_status[index] = max_health_capacity


def status():
    counter = 0
    for section in pirate_ship_status:
        if section < (0.20 * max_health_capacity):
            counter += 1
    return f"{counter} sections need repair."


pirate_ship_status = list(map(int, input().split('>')))
warship_status = list(map(int, input().split('>')))
max_health_capacity = int(input())
instruction = input()

is_end = False

while instruction != 'Retire':
    instruction = instruction.split()
    command = instruction[0]
    if command == 'Fire':
        if fire():
            print(f"You won! The enemy ship has sunken.")
            is_end = True
            break

    elif command == 'Defend':
        if defend():
            print(f"You lost! The pirate ship has sunken.")
            is_end = True
            break
    elif command == 'Repair':
        repair()

    elif command == 'Status':
        print(status())

    instruction = input()

if not is_end:
    pirate_ship_sum = sum(pirate_ship_status)
    warship_sum = sum(warship_status)
    print(f"""Pirate ship status: {pirate_ship_sum}
Warship status: {warship_sum}""")
