import math

sequence_of_number = list(map(int, input().split(', ')))
max_age = math.ceil(max(sequence_of_number) / 10)

for group_age in range(1, max_age + 1):
    group_age_list = []
    for number in sequence_of_number:
        current_age = number
        if current_age <= group_age * 10:
            group_age_list.append(current_age)
    for age in group_age_list:
        sequence_of_number.remove(age)
    print(f"Group of {group_age*10}'s: {group_age_list}")
