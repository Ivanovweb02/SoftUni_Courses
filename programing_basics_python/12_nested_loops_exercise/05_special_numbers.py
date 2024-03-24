number = int(input())

for current_number in range(1111, 10000):
    current_number_to_str = str(current_number)

    is_special = True
    for _, digit in enumerate(current_number_to_str):
        digit_as_int = int(digit)

        if digit_as_int == 0:
            is_special = False
            break

        if number % digit_as_int != 0:
            is_special = False
            break

    if is_special:
        print(f"{current_number}", end=" ")
