list_of_numbers = input().split()
number_as_digit = []
for number in list_of_numbers:
    number_as_digit.append(int(number))

print(f"The minimum number is {min(number_as_digit)}")
print(f"The maximum number is {max(number_as_digit)}")
print(f"The sum number is: {sum(number_as_digit)}")
