def rounded_numbers(list_of_numbers):
    list_rounded_numbers = []
    for number in list_of_numbers:
        list_rounded_numbers.append(round(number))
    return list_rounded_numbers


list_of_current_number = list(map(float, input().split()))
print(rounded_numbers(list_of_current_number))
