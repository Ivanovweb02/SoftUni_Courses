first_end = int(input())
second_end = int(input())
third_end = int(input())

for first_number in range(1, first_end + 1):
    for second_number in range(1, second_end + 1):
        is_prime = True
        if 2 <= second_number <= 7:
            for i in range(2, int(second_number/2) + 1):
                if (second_number % i) == 0:
                    is_prime = False
        elif second_number < 2 or second_end > 7:
            is_prime = False
        for third_number in range(1, third_end + 1):
            if first_number % 2 == 0 and third_number % 2 == 0 \
                    and is_prime:
                print(f'{first_number} {second_number} {third_number}')
