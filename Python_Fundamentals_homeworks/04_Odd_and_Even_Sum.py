def sum_of_numbers(num: str):
    sum_of_odd_numbers = 0
    sum_of_even_numbers = 0
    for digit in number:
        if int(digit) % 2 == 0:
            sum_of_even_numbers += int(digit)
        else:
            sum_of_odd_numbers += int(digit)
    return sum_of_odd_numbers, sum_of_even_numbers


number = input()
sum_of_odd, sum_of_even = sum_of_numbers(number)
print(f"Odd sum = {sum_of_odd}, Even sum = {sum_of_even}")
