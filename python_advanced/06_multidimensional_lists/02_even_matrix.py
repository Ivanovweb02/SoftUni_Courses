rows = int(input())
matrix_of_even_nums = []

for _ in range(rows):
    matrix_of_even_nums.append([int(x) for x in input().split(', ') if int(x) % 2 == 0])

print(matrix_of_even_nums)
