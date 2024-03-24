rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
coordinates = ((int(x) for x in c.split(',')) for c in input().split())

directions = (
    (-1, 0),   # Up
    (1, 0),    # Down
    (0, -1),   # Left
    (0, 1),    # Right
    (-1, 1),   # Top-Right
    (-1, -1),  # Top-Left
    (1, -1),   # Bottom-Left
    (1, 1),    # Bottom-Right
    (0, 0)     # Current-Position
)

for row, col in coordinates:
    if matrix[row][col] <= 0:
        continue
    for x, y in directions:
        curr_row, curr_col = row + x, col + y

        if 0 <= curr_row < rows and 0 <= curr_col < rows:
            matrix[curr_row][curr_col] -= matrix[row][col] if matrix[curr_row][curr_col] > 0 else 0

alive_cells = [num for row in range(rows) for num in matrix[row] if num > 0]
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*row) for row in matrix]
