import math

tournaments_count = int(input())
start_point = int(input())
tournaments_won = 0
earned_point = 0
for _ in range(1, tournaments_count +1 ):
    stage_of_tournament = input()
    if stage_of_tournament == "W":
        tournaments_won += 1
        earned_point += 2000
    elif stage_of_tournament == "F":
        earned_point += 1200
    elif stage_of_tournament == "SF":
        earned_point += 720

total_points = start_point + earned_point
avg_point_per_tournament = math.floor(earned_point / tournaments_count)
percent_won_tournaments = tournaments_won / tournaments_count * 100
print(f"Final points: {total_points}")
print(f"Average points: {avg_point_per_tournament}")
print(f"{percent_won_tournaments :.2f}%")
