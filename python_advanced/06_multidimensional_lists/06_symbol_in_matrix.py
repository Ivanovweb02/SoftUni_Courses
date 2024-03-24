rows = int(input())
square_matrix = []

for _ in range(rows):
    square_matrix.append(list(input()))

symbol = input()


for row in range(rows):
    for col in range(len(square_matrix[row])):
        char = square_matrix[row][col]
        if char == symbol:
            is_symbol_found = True
            print(f"({row}, {col})")
            exit()

print(f"{symbol} does not occur in the matrix")
