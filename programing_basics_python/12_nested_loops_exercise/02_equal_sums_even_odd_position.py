first_number = int(input())
second_number = int(input())

for number in range(first_number, second_number + 1):
    number_to_str = str(number)
    sum_of_even = 0
    sum_of_odd = 0
    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            sum_of_odd += int(digit)
        else:
            sum_of_even += int(digit)

    if sum_of_even == sum_of_odd:
        print(number, end=' ')
