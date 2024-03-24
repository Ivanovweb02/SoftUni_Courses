command = input()
won = 0
lose = 0
total_games = 0
while command != "End of tournaments":
    name_of_tournament = command
    count_games = int(input())
    total_games += count_games
    for current_count in range (1, count_games + 1):
        point_from_team = int(input())
        point_from_opponent = int(input())
        if point_from_team > point_from_opponent:
            diff = point_from_team - point_from_opponent
            won += 1
            print(f"Game {current_count} of tournament {name_of_tournament}: win with {diff} points.")
        else:
            diff = point_from_opponent - point_from_team
            lose += 1
            print(f"Game {current_count} of tournament {name_of_tournament}: lost with {diff} points.")

    command = input()

percent_won = won / total_games * 100
percent_lose = lose / total_games * 100
print(f"{percent_won :.2f}% matches win")
print(f"{percent_lose :.2f}% matches lost")
