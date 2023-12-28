number = int(input())

for current_number in range(1, number + 1):
    digit_sum = 0
    current_number_to_str = str(current_number)
    is_special = False
    for digit in current_number_to_str:
        digit_sum += int(digit)
        if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
            is_special = True
    print(f"{current_number} -> {is_special}")
