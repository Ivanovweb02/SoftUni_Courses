number_of_rows = int(input())
list_of_filed = []
count_of_destroyed_ship = 0
for _ in range(number_of_rows):
    current_row = list(map(int, input().split()))
    list_of_filed.append(current_row)

attacked_squares = input().split()
for current_square in attacked_squares:
    row, col = list(map(int, current_square.split('-')))
    current_target = list_of_filed[row][col]
    if current_target > 0:
        list_of_filed[row][col] -= 1
        if list_of_filed[row][col] == 0:
            count_of_destroyed_ship += 1

print(count_of_destroyed_ship)
