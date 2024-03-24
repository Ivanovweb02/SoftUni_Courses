rows, cols = [int(x) for x in input().split()]
square_matrix = []

for _ in range(rows):
    square_matrix.append([el for el in input().split()])

counter = 0
for row in range(rows - 1):
    for col in range(cols - 1):
        first_char = square_matrix[row][col]
        second_char = square_matrix[row][col + 1]
        third_char = square_matrix[row + 1][col]
        fourth_char = square_matrix[row + 1][col + 1]
        if first_char == second_char == third_char == fourth_char:
            counter += 1

print(counter)
