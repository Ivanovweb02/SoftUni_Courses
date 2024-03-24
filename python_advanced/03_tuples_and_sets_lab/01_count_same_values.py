list_of_numbers = tuple([float(num) for num in input().split()])
dict_number = {}

for num in list_of_numbers:
    if num not in dict_number:
        dict_number[num] = list_of_numbers.count(num)
        print(f"{num} - {dict_number[num]} times")
