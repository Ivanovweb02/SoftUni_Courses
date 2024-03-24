def extra_generous(presents_count):
    for way in directions:
        curr_r = santa_pos[0] + directions[way][0]
        curr_c = santa_pos[1] + directions[way][1]

        if neighborhood[curr_r][curr_c] == 'V' \
                or neighborhood[curr_r][curr_c] == 'X':
            neighborhood[curr_r][curr_c] = '-'
            presents_count += 1

    return presents_count


def santa_move(direction, presents_count=0):
    curr_row = santa_pos[0] + directions[direction][0]
    curr_col = santa_pos[1] + directions[direction][1]
    santa_pos[0], santa_pos[1] = curr_row, curr_col

    if neighborhood[curr_row][curr_col] == 'V':
        neighborhood[curr_row][curr_col] = '-'
        presents_count = 1

    elif neighborhood[curr_row][curr_col] == 'X':
        neighborhood[curr_row][curr_col] = '-'

    elif neighborhood[curr_row][curr_col] == 'C':
        neighborhood[curr_row][curr_col] = '-'
        presents_count = extra_generous(presents_count)

    return presents_count


presents = int(input())
size = int(input())

neighborhood = []
santa_pos = []

total_nice_kid = 0

for row in range(size):
    neighborhood.append(input().split())

    if 'S' in neighborhood[row]:
        santa_pos = [row, neighborhood[row].index('S')]
        neighborhood[santa_pos[0]][santa_pos[1]] = '-'
    total_nice_kid += neighborhood[row].count('V')

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

command = input()
while command != "Christmas morning":

    presents -= santa_move(command, 0)
    if presents <= 0:
        break

    command = input()

remaining_nice_kid = sum([row.count('V') for row in neighborhood])
neighborhood[santa_pos[0]][santa_pos[1]] = 'S'

if presents <= 0 and remaining_nice_kid:
    print("Santa ran out of presents!")

[print(*row) for row in neighborhood]

if remaining_nice_kid == 0:
    print(f"Good job, Santa! {total_nice_kid} happy nice kid/s.")
else:
    print(f"No presents for {remaining_nice_kid} nice kid/s.")
