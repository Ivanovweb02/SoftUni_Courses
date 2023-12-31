capacity = 255
number_of_lines = int(input())
count_of_water = 0
for lines in range(number_of_lines):
    liters_of_water = int(input())
    if capacity >= liters_of_water:
        capacity -= liters_of_water
        count_of_water += liters_of_water
    else:
        print("Insufficient capacity!")
        continue
print(count_of_water)
