row = int(input())
flattened_matrix = []

for _ in range(row):
    row_data = [int(x) for x in input().split(', ')]
    flattened_matrix.extend(row_data)

print(flattened_matrix)
