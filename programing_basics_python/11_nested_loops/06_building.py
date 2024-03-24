number_of_floor = int(input())
number_of_room = int(input())
letter = ""

for current_floor in range(number_of_floor, 0, -1):
    if current_floor == number_of_floor:
        letter = "L"
    elif current_floor % 2 == 0:
        letter = "O"
    else:
        letter = "A"
    for current_room in range(number_of_room):
        print(f"{letter}{current_floor}{current_room}", end=" ")
    print()
