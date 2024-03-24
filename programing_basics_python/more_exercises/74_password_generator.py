n = int(input())
l = int(input())

for first in range(1, n):
    for second in range(1, n):
        for third in range(97, (l + 97)):    #chr(97) = 'a'
            for fourth in range(97, (l + 97)):
                for fifth in range(1, n + 1):
                    if fifth > first and fifth > second:
                        print(f'{first}{second}{chr(third)}{chr(fourth)}{fifth}', end=' ')
