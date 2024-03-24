def add_bunnies(bunnies_poss):
    bunny_row, bunny_col = 0, 0
    for bunny_r, bunny_c in bunnies_poss:
        for curr_r, curr_c in directions.values():
            bunny_row, bunny_col = bunny_r + curr_r, bunny_c + curr_c
            if 0 <= bunny_row < rows and 0 <= bunny_col < cols:
                matrix[bunny_row][bunny_col] = 'B'

    return bunny_row, bunny_col


def find_bunnies():
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'B':
                bunnies_poss.append((r, c))
    return bunnies_poss


rows, cols = [int(x) for x in input().split()]
matrix = []
player_pos = []
bunnies_poss = []
directions = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}

for row in range(rows):
    matrix.append(list(input()))
    if 'P' in matrix[row]:
        player_pos = [row, matrix[row].index('P')]
        matrix[player_pos[0]][player_pos[1]] = '.'

won = False
commands = input()
status = ''
for command in commands:
    cur_row, cur_col = player_pos[0] + directions[command][0], player_pos[1] + directions[command][1]
    curr_bunny_row, curr_bunny_col = add_bunnies(find_bunnies())

    if cur_row < 0 or cur_row >= rows or cur_col < 0 or cur_col >= cols:
        status = 'won'

    elif (curr_bunny_row == cur_row and curr_bunny_col == cur_col) \
            or matrix[cur_row][cur_col] == 'B':
        player_pos = cur_row, cur_col
        status = 'dead'

    if status != '':
        [print(*row, sep='') for row in matrix]
        print(f"{status}: {player_pos[0]} {player_pos[1]}")
        break
    player_pos = cur_row, cur_col
