import sys

easter_bread_count = int(input())
highest_point = -sys.maxsize
winner_name = ""

for _ in range(1, easter_bread_count + 1):
    name_of_baker = input()
    command = input()
    point = 0

    while command != "Stop":
        easter_bread_rate = int(command)
        point += easter_bread_rate

        command = input()
    print(f"{name_of_baker} has {point} points.")
    if point > highest_point:
        winner_name = name_of_baker
        highest_point = point
        print(f"{name_of_baker} is the new number 1!")

print(f"{winner_name} won competition with {highest_point} points!")
