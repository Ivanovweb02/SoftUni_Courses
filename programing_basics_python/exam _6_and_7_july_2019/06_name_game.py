command = input()
winner = ""
max_point = 0

while command != "Stop":
    player_name = command
    point = 0
    for chart in player_name:
        number = int(input())
        ascii_value = ord(chart)
        if ascii_value == number:
            point += 10
        else:
            point += 2

    if point >= max_point:
        max_point = point
        winner = player_name

    command = input()

print(f"The winner is {winner} with {max_point} points!")
