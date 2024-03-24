def factorial_division(first_num: int, second_num: int) -> float or int:
    first_factorial = 1
    second_factorial = 1
    for number_1 in range(1, first_num + 1):
        first_factorial *= number_1
    for number_2 in range(1, second_num + 1):
        second_factorial *= number_2
    return first_factorial / second_factorial


first_number = int(input())
second_number = int(input())
print(f"{factorial_division(first_number, second_number) :.2f}")
