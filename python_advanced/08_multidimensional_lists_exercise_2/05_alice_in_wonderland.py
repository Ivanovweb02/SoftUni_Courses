n = int(input())
matrix = []
alice_pos = []

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

for row in range(n):
    matrix.append(input().split())
    if 'A' in matrix[row]:
        alice_pos = [row, matrix[row].index('A')]
        matrix[alice_pos[0]][alice_pos[1]] = '*'

collected_tea = 0
while collected_tea < 10:
    command = input()
    curr_row, curr_col = alice_pos[0] + directions[command][0], alice_pos[1] + directions[command][1]
    if 0 <= curr_row < n and 0 <= curr_col < n:
        if matrix[curr_row][curr_col] == 'R':
            matrix[curr_row][curr_col] = '*'
            break
        alice_pos = [curr_row, curr_col]
        if matrix[curr_row][curr_col].isdigit():
            collected_tea += int(matrix[curr_row][curr_col])
        matrix[curr_row][curr_col] = '*'
    else:
        break

if collected_tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*row) for row in matrix]
