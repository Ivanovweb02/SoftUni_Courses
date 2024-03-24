a1 = int(input())
a2 = int(input())
n = int(input())

for first_symbol in range(a1, a2):
    for second_symbol in range(1, n):
        for third_symbol in range(1, int(n/2)):
            fourth_symbol = first_symbol
            total = second_symbol + third_symbol + fourth_symbol
            if first_symbol % 2 != 0 and total % 2 != 0:
                print(f"{chr(first_symbol)}-{second_symbol}{third_symbol}{fourth_symbol}")
