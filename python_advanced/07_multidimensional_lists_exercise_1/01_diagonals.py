rows = int(input())
square_matrix = []
primary_diagonals = []
secondary_diagonals = []
for row in range(rows):
    row_data = [int(x) for x in input().split(', ')]
    square_matrix.append(row_data)
    primary_diagonals.append(row_data[row])
    secondary_diagonals.append(row_data[(len(row_data) - 1) - row])

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonals)}. Sum: {sum(primary_diagonals)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonals)}. Sum: {sum(secondary_diagonals)}")
