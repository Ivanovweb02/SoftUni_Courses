import math
import sys


def get_distance(first_coordinate: int, second_coordinate: int) -> int:
    return abs(first_coordinate) + abs(second_coordinate)


def longest_points(some_list: list):
    max_value_1 = -sys.maxsize
    max_value_2 = -sys.maxsize
    for element in some_list:
        if element > max_value_1:
            max_value_1 = element
        elif element > max_value_2:
            max_value_2 = element
    return max_value_2, max_value_1


x_1, y_1 = math.floor(float(input())), math.floor(float(input()))
x_2, y_2 = math.floor(float(input())), math.floor(float(input()))
x_3, y_3 = math.floor(float(input())), math.floor(float(input()))
x_4, y_4 = math.floor(float(input())), math.floor(float(input()))


first_point = get_distance(x_1, y_1)
second_point = get_distance(x_2, y_2)
third_point = get_distance(x_3, y_3)
fourth_point = get_distance(x_4, y_4)
list_of_point = [first_point, second_point, third_point, fourth_point]

value = longest_points(list_of_point)
if value[0] == first_point:
    print(f"({x_1}, {y_1})", end='')
    if value[1] == second_point:
        print(f"({x_2}, {y_2})")
    elif value[1] == third_point:
        print(f"({x_3}, {y_3})")
    elif value[1] == fourth_point:
        print(f"({x_4}, {y_4})")


elif value[0] == second_point:
    print(f"({x_2}, {y_2})", end='')
    if value[1] == first_point:
        print(f"({x_1}, {y_1})")
    elif value[1] == third_point:
        print(f"({x_3}, {y_3})")
    elif value[1] == fourth_point:
        print(f"({x_4}, {y_4})")

elif value[0] == third_point:
    print(f"({x_3}, {y_3})", end='')
    if value[1] == first_point:
        print(f"({x_1}, {y_1})")
    elif value[1] == second_point:
        print(f"({x_2}, {y_2})")
    elif value[1] == fourth_point:
        print(f"({x_4}, {y_4})")
elif value[0] == fourth_point:
    print(f"({x_4}, {y_4})", end='')
    if value[1] == first_point:
        print(f"({x_1}, {y_1})")
    elif value[1] == second_point:
        print(f"({x_2}, {y_2})")
    elif value[1] == third_point:
        print(f"({x_3}, {y_3})")
