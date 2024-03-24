first_number = int(input())
second_number = int(input())
third_number = int(input())

for first in range(1, first_number + 1):
    for second in range(1, second_number + 1):
        is_prime = True
        if 2 <= second <= 7:
            for i in range(2, int(second/2) + 1):
                if (second % i) == 0:
                    is_prime = False

            for third in range(1, third_number + 1):
                if first % 2 == 0 and third % 2 == 0 and is_prime:
                    print(f"{first} {second} {third}")
