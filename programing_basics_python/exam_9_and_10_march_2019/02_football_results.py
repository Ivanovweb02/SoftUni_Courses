total_matches = 3

won_games = 0
lost_games = 0
drawn_games = 0

for _ in range(1, total_matches + 1):
    result_of_match = input()
    if ord(result_of_match[0]) > ord(result_of_match[2]):
        won_games += 1
    elif ord(result_of_match[0]) < ord(result_of_match[2]):
        lost_games += 1
    else:
        drawn_games += 1

print(f"Team won {won_games} games.")
print(f"Team lost {lost_games} games.")
print(f"Drawn games: {drawn_games}")
