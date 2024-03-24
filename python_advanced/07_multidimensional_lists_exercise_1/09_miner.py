def is_end(r, c):
    if matrix[curr_row][curr_col] == 'e':
        print(f"Game over! ({curr_row}, {curr_col})")
        return True
    return False


def is_collected(r, c):
    if collected_coal == total_coal:
        print(f"You collected all coal! ({r}, {c})")
        return True
    return False


def check_position(r, c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


n = int(input())
commands = input().split()
matrix = []
miner_poss = []
total_coal = 0
collected_coal = 0

directions = {
    'left': [0, -1],
    'right': [0, 1],
    'up': [-1, 0],
    'down': [1, 0]
}

for row in range(n):
    matrix.append(input().split())

    if 's' in matrix[row]:
        miner_poss = [row, matrix[row].index('s')]
        matrix[miner_poss[0]][miner_poss[1]] = '*'

    total_coal += matrix[row].count('c')

for command in commands:
    curr_row, curr_col = miner_poss[0] + directions[command][0], miner_poss[1] + directions[command][1]
    if check_position(curr_row, curr_col):
        miner_poss = [curr_row, curr_col]
        if matrix[curr_row][curr_col] == 'c':
            matrix[curr_row][curr_col] = '*'
            collected_coal += 1
        if is_collected(curr_row, curr_col):
            break
        if is_end(curr_row, curr_col):
            break
else:
    print(f"{total_coal - collected_coal} pieces of coal left. ({miner_poss[0]}, {miner_poss[1]})")
