hall_capacity = int(input())
command = input()

total_people = 0
is_full = False

total_price = 0

while command != "Movie time!":
    people_count = int(command)
    total_people += people_count
    if total_people > hall_capacity:
        is_full = True
        break
    total_price += people_count * 5
    if people_count % 3 == 0:
        total_price -= 5

    command = input()

if is_full:
    print("The cinema is full.")
else:
    left_seat = hall_capacity - total_people
    print(f"There are {left_seat} seats left in the cinema.")

print(f"Cinema income - {total_price} lv.")
