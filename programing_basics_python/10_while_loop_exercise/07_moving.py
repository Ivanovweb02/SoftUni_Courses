width = int(input())
length = int(input())
height = int(input())

total_space = width * length * height

command = input()
while command != "Done":
    count_of_boxes = int(command)
    total_space -= count_of_boxes
    if total_space <= 0:
        break

    command = input()

if command == "Done":
    left_space = total_space
    print(f"{left_space} Cubic meters left.")
else:
    needed_space = abs(total_space)
    print(f"No more free space! You need {needed_space} Cubic meters more.")
