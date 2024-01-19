first_number, second_number, third_number = int(input()), int(input()), int(input())
list_of_numbers = [first_number, second_number, third_number]

result = 'positive'
negative_count = 0
for number in list_of_numbers:
    if number < 0:
        negative_count += 1
        if negative_count % 2 != 0:
            result = 'negative'
        else:
            result = 'positive'
    elif number == 0:
        result = 'zero'
        break

print(result)
