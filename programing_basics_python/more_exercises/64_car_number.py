start = int(input())
end = int(input())

for first_number in range(start, end + 1):
    for second_number in range(start, end + 1):
        for third_number in range(start, end + 1):
            for fourth_number in range(start, end + 1):
                is_spacial = False
                if ((first_number % 2 == 0 and fourth_number % 2 != 0)
                        or (fourth_number % 2 == 0 and first_number % 2 != 0)) \
                        and first_number > fourth_number \
                        and (second_number + third_number) % 2 == 0:
                    is_spacial = True
                if is_spacial:
                    print(f"{first_number}{second_number}{third_number}{fourth_number}", end=" ")
