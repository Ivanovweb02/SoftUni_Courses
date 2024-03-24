row, col = [int(x) for x in input().split(', ')]

matrix = []
matrix_sum = 0
for _ in range(row):
    curr_row = [int(x) for x in input().split(', ')]
    matrix.append(curr_row)
    matrix_sum += sum(curr_row)

print(matrix_sum)
print(matrix)
