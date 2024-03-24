some_list = [[int(y)for y in x.split()] for x in input().split('|')]
some_list = reversed(some_list)
[print(*x, sep=' ', end=' ') for x in some_list if x]
