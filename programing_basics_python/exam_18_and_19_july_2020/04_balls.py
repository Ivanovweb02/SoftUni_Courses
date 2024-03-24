import math

number = int(input())
total_point = 0
red_balls = 0
orange_ball = 0
yellow_ball = 0
white_ball = 0
black_ball = 0
other_color = 0

for _ in range(1, number + 1):
    color = input()
    if color == "red":
        red_balls += 1
        total_point += 5
    elif color == "orange":
        orange_ball += 1
        total_point += 10
    elif color == "yellow":
        yellow_ball += 1
        total_point += 15
    elif color == "white":
        white_ball += 1
        total_point += 20
    elif color == "black":
        black_ball += 1
        total_point = math.floor(total_point / 2)
    else:
        other_color += 1

print(f"Total points: {total_point}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_ball}")
print(f"Yellow balls: {yellow_ball}")
print(f"White balls: {white_ball}")
print(f"Other colors picked: {other_color}")
print(f"Divides from black balls: {black_ball}")
