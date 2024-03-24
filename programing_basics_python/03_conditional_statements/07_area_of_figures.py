import math

figure_type = input()

if figure_type == "square":
    length_of_side = float(input())
    area = length_of_side ** 2

elif figure_type == "rectangle":
    length_of_side_1 = float(input())
    length_of_side_2 = float(input())
    area = length_of_side_1 * length_of_side_2

elif figure_type == "circle":
    radius = float(input())
    area = radius ** 2 * math.pi

elif figure_type == "triangle":
    length_of_side = float(input())
    length_of_height = float(input())
    area = length_of_side * length_of_height / 2

print(f"{area :.2f}")
