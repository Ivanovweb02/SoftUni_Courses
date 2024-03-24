count_of_move = int(input())
point = 0
counter_to_9 = 0
counter_to_19 = 0
counter_to_29 = 0
counter_to_39 = 0
counter_to_50 = 0
invalid_numbers = 0
for _ in range(1, count_of_move + 1):
    interval = int(input())
    if 0 <= interval <= 9:
        counter_to_9 += 1
        point += interval * 0.20
    elif 10 <= interval <= 19:
        counter_to_19 += 1
        point += interval * 0.30
    elif 20 <= interval <= 29:
        counter_to_29 += 1
        point += interval * 0.40
    elif 30 <= interval <= 39:
        counter_to_39 += 1
        point += 50
    elif 40 <= interval <= 50:
        counter_to_50 += 1
        point += 100
    else:
        invalid_numbers += 1
        point /= 2

percent_to_9 = counter_to_9 / count_of_move * 100
percent_to_19 = counter_to_19 / count_of_move * 100
percent_to_29 = counter_to_29 / count_of_move * 100
percent_to_39 = counter_to_39 / count_of_move * 100
percent_to_50 = counter_to_50 / count_of_move * 100
percent_invalid_numbers = invalid_numbers / count_of_move * 100

print(f"{point :.2f}")
print(f"From 0 to 9: {percent_to_9 :.2f}%")
print(f"From 10 to 19: {percent_to_19 :.2f}%")
print(f"From 20 to 29: {percent_to_29 :.2f}%")
print(f"From 30 to 39: {percent_to_39 :.2f}%")
print(f"From 40 to 50: {percent_to_50 :.2f}%")
print(f"Invalid numbers: {percent_invalid_numbers :.2f}%")
