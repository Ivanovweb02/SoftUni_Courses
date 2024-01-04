def smallest_number(first: int, second: int, third: int) -> int:
    list_of_number = [first, second, third]
    return min(list_of_number)


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(smallest_number(first_number, second_number, third_number))
