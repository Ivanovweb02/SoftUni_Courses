n = int(input())
matrix = []
bunny_pos = []

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}
taken_direction = ''
max_egg = float('-inf')
path = []
for row in range(n):
    matrix.append(input().split())
    if 'B' in matrix[row]:
        bunny_pos = [row, matrix[row].index('B')]

for direction in directions:

    curr_row, curr_col = bunny_pos[0] + directions[direction][0], bunny_pos[1] + directions[direction][1]
    collected_egg = 0
    curr_path = []

    while 0 <= curr_row < n and 0 <= curr_col < n:
        if matrix[curr_row][curr_col] != 'X':
            collected_egg += int(matrix[curr_row][curr_col])
        else:
            break
        curr_path.append([curr_row, curr_col])
        curr_row, curr_col = curr_row + directions[direction][0], curr_col + directions[direction][1]

    if collected_egg > max_egg and curr_path:
        taken_direction = direction
        max_egg = collected_egg
        path = curr_path

print(taken_direction)
[print(row) for row in path]
print(max_egg)
