class ValueCannotBeNegative(Exception):
    pass


COUNT = 5

for _ in range(COUNT):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative
