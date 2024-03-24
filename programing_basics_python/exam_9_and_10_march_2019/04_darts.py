player_name = input()
command = input()
start_point = 301
shots = 0
unsuccessful_shots = 0
is_he_won = False
while command != "Retire":
    field = command
    point = int(input())
    if field == "Single":
        if point <= start_point:
            shots += 1
            start_point -= point
        else:
            unsuccessful_shots += 1
    elif field == "Double":
        if point * 2 <= start_point:
            shots += 1
            start_point -= point * 2
        else:
            unsuccessful_shots += 1
    elif field == "Triple":
        if point * 3 <= start_point:
            shots += 1
            start_point -= point * 3
        else:
            unsuccessful_shots += 1

    if start_point == 0:
        is_he_won = True
        break
    command = input()

if is_he_won:
    print(f"{player_name} won the leg with {shots} shots.")
else:
    print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")
