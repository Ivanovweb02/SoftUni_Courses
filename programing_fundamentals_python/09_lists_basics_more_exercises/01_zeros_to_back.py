list_of_number = list(map(int, input().split(', ')))
list_of_zeros = []

for digit in range(len(list_of_number) - 1, -1, -1):
    if list_of_number[digit] == 0:
        list_of_zeros.append(list_of_number[digit])
        list_of_number.pop(digit)

for zero in list_of_zeros:
    list_of_number.append(zero)

print(list_of_number)
