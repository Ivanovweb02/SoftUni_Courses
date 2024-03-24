import cmath

rows, cols = [int(x) for x in input().split()]

rectangular_matrix = []
max_sum = -cmath.inf
max_3x3_square = []

for _ in range(rows):
    rectangular_matrix.append([int(x) for x in input().split()])

for row in range(rows - 2):
    for col in range(cols - 2):
        first_row = rectangular_matrix[row][col:col+3]
        second_row = rectangular_matrix[row + 1][col:col+3]
        third_row = rectangular_matrix[row + 2][col:col+3]

        total_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if total_sum > max_sum:
            max_3x3_square = [first_row, second_row, third_row]
            max_sum = total_sum

print(f"Sum = {max_sum}")
[print(*row) for row in max_3x3_square]
