command = input()
prime_number = 0
nonprime_number = 0

while command != "stop":
    number = int(command)
    if number < 0:
        print("Number is negative.")
        command = input()
        continue
    is_prime = True
    for current_number in range(2, number):
        if number % current_number == 0:
            is_prime = False
            break

    if is_prime:
        prime_number += number
    else:
        nonprime_number += number

    command = input()

print(f"Sum of all prime numbers is: {prime_number}")
print(f"Sum of all non prime numbers is: {nonprime_number}")
