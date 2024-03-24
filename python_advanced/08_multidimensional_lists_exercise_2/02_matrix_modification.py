def subtract_data(r, c, v):
    matrix[r][c] -= v


def check_data(r, c):
    if 0 <= r < len(matrix) and 0 <= c < len(matrix):
        return True
    return False


def add_data(r, c, v):
    matrix[r][c] += v


n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

instruction = input()

while instruction != 'END':
    command, *data = instruction.split()
    data = [int(x) for x in data]
    row, col, value = data

    if check_data(row, col):
        if command == 'Add':
            add_data(row, col, value)
        elif command == 'Subtract':
            subtract_data(row, col, value)
    else:
        print('Invalid coordinates')

    instruction = input()

[print(*row, sep=' ') for row in matrix]
