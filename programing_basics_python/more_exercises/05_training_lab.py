height = float(input())
width = float(input())

height *= 100
width *= 100

current_width = width - 100
desks_in_a_row = current_width // 70

count_of_rows = height // 120

count_of_seats = desks_in_a_row * count_of_rows - 3
print(int(count_of_seats))
