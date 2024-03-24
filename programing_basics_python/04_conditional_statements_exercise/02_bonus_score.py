starting_number_of_points = int(input())
bonus_point = 0
if starting_number_of_points <= 100:
    bonus_point = 5
elif 1000 >= starting_number_of_points > 100:
    bonus_point = 0.20 * starting_number_of_points
else:
    bonus_point = 0.10 * starting_number_of_points

if starting_number_of_points % 2 == 0:
    bonus_point = bonus_point + 1

if starting_number_of_points % 10 == 5:    # or starting_number_of_point% 5 == 0:
    bonus_point = bonus_point + 2

print(bonus_point)
print(starting_number_of_points + bonus_point)
