rows = int(input())
square_matrix = []
diagonals_sum = 0

for row in range(rows):
    row_data = [int(x) for x in input().split()]
    square_matrix.append(row_data)
    diagonals_sum += row_data[row]

print(diagonals_sum)


# opposite diagonal
# rows = int(input())
# square_matrix = []
# diagonals_sum = 0
#
# for row in range(rows - 1, -1, -1):
#     row_data = [int(x) for x in input().split()]
#     square_matrix.append(row_data)
#     diagonals_sum += row_data[row]
#
# print(diagonals_sum)
