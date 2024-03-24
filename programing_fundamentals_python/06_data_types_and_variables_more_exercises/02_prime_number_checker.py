number = int(input())
is_prime = True

if number != 1:
    for digit in range(2, int(number/2)):
        if  number % digit == 0:
            is_prime = False
            break
else:
    is_prime = False

print(is_prime)
