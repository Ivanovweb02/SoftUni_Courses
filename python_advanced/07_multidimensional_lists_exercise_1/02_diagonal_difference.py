rows = int(input())
first_diagonal = []
second_diagonal = []

for row in range(rows):
    row_data = [int(x) for x in input().split()]
    first_diagonal.append(row_data[row])
    second_diagonal.append(row_data[(rows - 1) - row])

diagonals_diff = abs(sum(first_diagonal) - sum(second_diagonal))
print(diagonals_diff)
