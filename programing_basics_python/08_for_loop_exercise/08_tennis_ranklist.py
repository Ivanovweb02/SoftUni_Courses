import math

count_of_tournaments = int(input())
starting_points = int(input())
received_points = 0
count_of_wins = 0
for _ in range(count_of_tournaments):
    stage_of_tournament = input()
    if stage_of_tournament == "W":
        received_points += 2000
        count_of_wins += 1
    elif stage_of_tournament == "F":
        received_points += 1200
    elif stage_of_tournament == "SF":
        received_points += 720

final_points = starting_points + received_points
average_points = math.floor(received_points / count_of_tournaments)
percent_of_wins = count_of_wins / count_of_tournaments * 100

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{percent_of_wins:.2f}%")
