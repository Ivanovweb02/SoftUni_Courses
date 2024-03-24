import math

room_height = int(input())
room_width = int(input())
percent_total_area = int(input())
command = input()

used_paint = 0
total_space = (room_width * room_height) * 4
total_space -= (percent_total_area / 100) * total_space

is_finished = False

while command != "Tired!":
    liter_paint = int(command)
    used_paint += liter_paint
    if used_paint >= total_space:
        is_finished = True
        break
    command = input()

if is_finished:
    left_paint = math.ceil(used_paint - total_space)
    if left_paint == 0:
        print("All walls are painted! Great job, Pesho!" )
    else:
        print(f"All walls are painted and you have {left_paint} l paint left!")

else:
    left_quadratic_meters = math.ceil(total_space - used_paint)
    print(f"{left_quadratic_meters} quadratic m left.")
