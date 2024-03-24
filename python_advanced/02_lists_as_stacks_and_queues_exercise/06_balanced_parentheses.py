from collections import deque

some_string = deque(input())
open_brackets = '([{'
close_brackets = ')]}'

counter = 0
while some_string and counter < len(some_string) / 2:
    if some_string[0] not in open_brackets:
        break
    index = open_brackets.index(some_string[0])
    if some_string[1] == close_brackets[index]:
        some_string.popleft()
        some_string.popleft()
        some_string.rotate(counter)
        counter = 0
    else:
        some_string.rotate(-1)
        counter += 1

if some_string:
    print('NO')
else:
    print('YES')
