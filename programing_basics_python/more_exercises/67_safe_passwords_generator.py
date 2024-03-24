a_symbol = int(input())
b_symbol = int(input())
max_times = int(input())
first_symbol = 35
second_symbol = 64
password_count = 0
is_max_times = False

for x_symbol in range(1, a_symbol + 1):
    if is_max_times:
        break
    for y_symbol in range(1, b_symbol + 1):
        password_count += 1
        if first_symbol > 55:
            first_symbol = 35
        if second_symbol > 96:
            second_symbol = 64
        print(f'{chr(first_symbol)}{chr(second_symbol)}'
              f'{x_symbol}{y_symbol}{chr(second_symbol)}{chr(first_symbol)}', end='|')
        first_symbol += 1
        second_symbol += 1
        if password_count == max_times:
            is_max_times = True
            break
