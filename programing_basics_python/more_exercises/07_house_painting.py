height_of_house = float(input())
length_of_house = float(input())
height_of_ceil = float(input())

front_wall = height_of_house**2
side_wall = length_of_house * height_of_house - 1.5**2
cost_of_green_paint = (front_wall * 2 - 1.2 * 2) + side_wall * 2
green_paint_per_liter = cost_of_green_paint / 3.4

front_of_ciel = height_of_house * height_of_ceil / 2
side_of_ciel = length_of_house * height_of_house
cost_of_red_paint = (front_of_ciel * 2) + (side_of_ciel * 2)
red_paint_per_liter = cost_of_red_paint / 4.3

print(f"{green_paint_per_liter:.2f}")
print(f"{red_paint_per_liter:.2f}")
