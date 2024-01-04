list_of_numbers = input().split()
number_as_digit = []
for number in list_of_numbers:
    number_as_digit.append(int(number))
list_of_sorted_number = sorted(number_as_digit)
print(list_of_sorted_number)

# solution_2:
# list_of_number = list(map(int, input().split()))
# sorted_list = sorted(list_of_number)
# print(sorted_list)
