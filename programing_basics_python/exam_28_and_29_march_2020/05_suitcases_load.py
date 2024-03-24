space = float(input())
command = input()
suitcase_count = 0
total_space = 0

is_space_full = False
while command != "End":
    suitcase_size = float(command)
    if total_space > space:
        is_space_full = True
        break
    suitcase_count += 1
    if suitcase_count % 3 == 0:
        suitcase_size += suitcase_size * 0.10
    total_space += suitcase_size

    if total_space > space:
        is_space_full = True
        suitcase_count -= 1
        break

    command = input()

if is_space_full:
    print("No more space!")
else:
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {suitcase_count} suitcases loaded.")
