start_first_couple = int(input())
start_second_couple = int(input())
first_diff_to_end = int(input())
second_diff_to_end = int(input())

for current_first_couple in range(start_first_couple, (start_first_couple + first_diff_to_end) + 1):
    for current_second_couple in range(start_second_couple, (start_second_couple + second_diff_to_end) + 1):
        is_first_couple_prime = True
        is_second_couple_prime = True
        for x in range(2, int(current_first_couple/2) + 1):
            if current_first_couple % x == 0:
                is_first_couple_prime = False
            for y in range(2, int(current_second_couple/2) + 1):
                if current_second_couple % y == 0:
                    is_second_couple_prime = False
        if is_first_couple_prime and is_second_couple_prime:
            print(f'{current_first_couple}{current_second_couple}')
