def number_classification(numbers):
    positive = [number for number in numbers if int(number) >= 0]
    negative = [number for number in numbers if int(number) < 0]
    even = [number for number in numbers if int(number) % 2 == 0]
    odd = [number for number in numbers if int(number) % 2 != 0]
    return f"Positive: {', '.join(positive)}\nNegative: {', '.join(negative)}" \
           f"\nEven: {', '.join(even)}\nOdd: {', '.join(odd)}"


list_of_numbers = input().split(', ')
print(number_classification(list_of_numbers))
