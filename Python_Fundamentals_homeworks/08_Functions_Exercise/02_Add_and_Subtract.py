def add_and_subtract(first: int, second: int, third: int) -> int:
    sum_of_number = first + second
    subtract_of_number = sum_of_number - third
    return subtract_of_number


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))
