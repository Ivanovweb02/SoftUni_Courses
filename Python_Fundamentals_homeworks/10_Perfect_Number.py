def is_perfect_number(some_number: int) -> list:
    list_of_divisors = []
    for divisor in range(1, some_number):
        if some_number % divisor == 0:
            list_of_divisors.append(divisor)
    return list_of_divisors


number = int(input())
divisors = is_perfect_number(number)
if sum(divisors) == number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
