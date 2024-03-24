start = int(input())
final = int(input())
magic_number = int(input())
counter_of_combination = 0
is_founded = False

for first_number in range(start, final +1):
    for second_number in range(start, final + 1):
        counter_of_combination += 1
        if first_number + second_number == magic_number:
            is_founded = True
            break
    if is_founded:
        break

if is_founded:
    print(f"Combination N:{counter_of_combination} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{counter_of_combination} combinations - neither equals {magic_number}")
