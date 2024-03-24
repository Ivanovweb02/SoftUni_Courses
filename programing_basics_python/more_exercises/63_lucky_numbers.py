number = int(input())

for first_number in range(1, 9 + 1):
    for second_number in range(1, 9 + 1):
        for third_number in range(1, 9 + 1):
            for fourth_number in range(1, 9 + 1):
                total = first_number + second_number
                if (first_number + second_number) == (third_number + fourth_number) \
                        and number % total == 0:
                    print(f'{first_number}{second_number}{third_number}{fourth_number}', end=' ')
