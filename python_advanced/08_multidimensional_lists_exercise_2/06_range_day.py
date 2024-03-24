def move_shooter(direc, s):
    curr_row = shooter_pos[0] + (directions[direc][0] * s)
    curr_col = shooter_pos[1] + (directions[direc][1] * s)

    if 0 <= curr_row < SIZE and 0 <= curr_col < SIZE:
        if matrix[curr_row][curr_col] == '.':
            shooter_pos[0], shooter_pos[1] = curr_row, curr_col


def shooting(direc):
    bullet_path = [shooter_pos[0], shooter_pos[1]]
    curr_r, curr_c = bullet_path[0] + directions[direc][0], bullet_path[1] + directions[direc][1]

    while 0 <= curr_r < SIZE and 0 <= curr_c < SIZE:
        if matrix[curr_r][curr_c] == 'x':
            targets.append([curr_r, curr_c])
            matrix[curr_r][curr_c] = '.'
            return 1

        bullet_path = [curr_r, curr_c]
        curr_r, curr_c = bullet_path[0] + directions[direc][0], bullet_path[1] + directions[direc][1]

    return 0


SIZE = 5
matrix = []
shooter_pos = []
total_target = 0
hit_target = 0
targets = []

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

for row in range(SIZE):
    matrix.append(input().split())

    if 'A' in matrix[row]:
        shooter_pos = [row, matrix[row].index('A')]
        matrix[shooter_pos[0]][shooter_pos[1]] = '.'

    total_target += matrix[row].count('x')

n = int(input())

for _ in range(n):
    command = input().split()
    direction = command[1]

    if 'move' in command:
        steps = int(command[2])
        move_shooter(direction, steps)

    elif 'shoot' in command:
        hit_target += shooting(direction)

        if hit_target == total_target:
            break

if hit_target == total_target:
    print(f"Training completed! All {hit_target} targets hit.")
else:
    print(f"Training not completed! {total_target - hit_target} targets left.")

[print(row) for row in targets]
