rows, cols = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

for col in range(cols):
    result = 0
    for row in range(rows):
        result += matrix[row][col]
    print(result)
