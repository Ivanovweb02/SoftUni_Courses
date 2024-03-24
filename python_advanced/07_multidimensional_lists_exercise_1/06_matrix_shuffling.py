def check_elements(coordinates):
    return {coordinates[0], coordinates[2]}.issubset(valid_rows) \
           and {coordinates[1], coordinates[3]}.issubset(valid_cols)


def swap_elements(action, coordinates):
    if len(coordinates) == 4 and check_elements(coordinates) and action == 'swap':
        row_1, col_1, row_2, col_2 = coordinates
        matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
        [print(*row) for row in matrix]

    else:
        print('Invalid input!')


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]
valid_rows = range(rows)
valid_cols = range(cols)

instruction = input()
while instruction != 'END':
    command, *data = [int(x) if x.isdigit() else x for x in instruction.split()]
    swap_elements(command, data)
    instruction = input()
