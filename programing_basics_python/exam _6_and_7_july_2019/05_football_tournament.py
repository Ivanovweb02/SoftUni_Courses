football_team = input()
played_games = int(input())
point = 0
wins = 0
draws = 0
loses = 0
for _ in range(1, played_games + 1):
    game_result = input()
    if game_result == "W":
        point += 3
        wins += 1
    elif game_result == "D":
        point += 1
        draws += 1
    elif game_result == "L":
        loses += 1

if played_games < 1:
    print(f"{football_team} hasn't played any games during this season.")

else:
    percent_wins = (wins / played_games) * 100
    print(f"{football_team} has won {point} points during this season.")
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {loses}")
    print(f"Win rate: {percent_wins :.2f}%")
