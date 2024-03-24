rows, cols = [int(x) for x in input().split(', ')]

matrix = []
biggest_nums = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

for row in range(rows - 1):
    for col in range(cols - 1):
        first_num = matrix[row][col]
        second_num = matrix[row][col + 1]
        third_num = matrix[row + 1][col]
        fourth_num = matrix[row + 1][col + 1]
        curr_sum = first_num + second_num + third_num + fourth_num
        if curr_sum > sum(biggest_nums):
            biggest_nums = [first_num, second_num, third_num, fourth_num]

for idx in range(0, len(biggest_nums), 2):
    print(f"{biggest_nums[idx]} {biggest_nums[idx + 1]}")

print(sum(biggest_nums))
