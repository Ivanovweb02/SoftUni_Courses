all_stops = input()
instructions = input()

while instructions != 'Travel':
    instructions = instructions.split(':')
    command = instructions[0]
    if command == 'Add Stop':
        index = int(instructions[1])
        string = instructions[2]
        if index < len(all_stops):
            all_stops = all_stops[:index] + string + all_stops[index:]
    elif command == 'Remove Stop':
        start_index = int(instructions[1])
        end_index = int(instructions[2])
        if start_index < len(all_stops) and end_index < len(all_stops):
            for index in range(end_index, start_index - 1, -1):
                char = all_stops[index]
                all_stops = all_stops.replace(char, "", 1)
    elif command == 'Switch':
        old_string = instructions[1]
        new_string = instructions[2]
        if old_string in all_stops:
            all_stops = all_stops.replace(old_string, new_string, 1)
    print(all_stops)

    instructions = input()

print(f"Ready for world tour! Planned stops: {all_stops}")
