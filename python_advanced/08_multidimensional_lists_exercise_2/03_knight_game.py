def check_movements(r, c, removed=0):
    for move in movements:
        curr_row, curr_col = r + move[0], c + move[1]
        if 0 <= curr_row < n and 0 <= curr_col < n:
            if chess_board[curr_row][curr_col] == 'K':
                removed += 1
    return removed


n = int(input())
chess_board = [list(input()) for _ in range(n)]

knights = {}

movements = [
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, -1),
    (2, 1),
    (1, -2),
    (1, 2)
]

coordinates = []
removed_knights = 0
while True:
    for row in range(n):
        for col in range(n):
            knight = 0
            if chess_board[row][col] == 'K':
                knight += check_movements(row, col, 0)
                knights[row, col] = knight

    is_end = True
    for value in knights.values():
        if value > 0:
            is_end = False
            break
    if is_end:
        break
    else:
        biggest_value = 0
        for coordinate, value in knights.items():
            if value > biggest_value:
                biggest_value = value
                coordinates = [coordinate[0], coordinate[1]]
        removed_knights += 1
        chess_board[coordinates[0]][coordinates[1]] = '0'
        knights[coordinates[0], coordinates[1]] = 0

print(removed_knights)
