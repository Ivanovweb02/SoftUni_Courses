sequence_of_numbers = input().split()
list_of_absolute_numbers = []

for number in sequence_of_numbers:
    list_of_absolute_numbers.append(abs(float(number)))
print(list_of_absolute_numbers)
