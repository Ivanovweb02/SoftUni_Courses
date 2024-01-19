import math


def coordination_point(first_coordinate: float, second_coordinate: float) -> str:
    first_coordinate = math.floor(first_coordinate)
    second_coordinate = math.floor(second_coordinate)
    return f"({first_coordinate}, {second_coordinate})"


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

first_position = abs(int(x_1)) + abs(int(y_1))
second_position = abs(int(x_2)) + abs(int(y_2))

if first_position <= second_position:
    print(coordination_point(x_1, y_1))
else:
    print(coordination_point(x_2, y_2))
