level_of_fire = input().split("#")
amount_of_water = int(input())
effort = 0
total_fire = 0
list_of_cells = []

for fire in level_of_fire:
    args = fire.split("=")
    fire_type = args[0]
    fire_value = int(args[1])
    value = False

    if fire_value > amount_of_water:
        continue

    if fire_type == "High " and 81 <= fire_value <= 125:
        value = True
    elif fire_type == "Medium " and 51 <= fire_value <= 80:
        value = True
    elif fire_type == "Low " and 1 <= fire_value <= 50:
        value = True
    if value:
        amount_of_water -= fire_value
        total_fire += fire_value
        effort += 0.25 * fire_value
        list_of_cells.append(fire_value)

print("Cells:")
for cells in list_of_cells:
    print(f" - {cells}")
print(f"Effort: {effort :.2f}")
print(f"Total Fire: {total_fire}")
