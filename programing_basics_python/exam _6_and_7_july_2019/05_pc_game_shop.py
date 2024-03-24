sold_games = int(input())

hearthstone_count = 0
fornite_count = 0
overwatch_count = 0
other_count = 0

for _ in range(1, sold_games + 1):
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone_count += 1
    elif game_name == "Fornite":
        fornite_count += 1
    elif game_name == "Overwatch":
        overwatch_count += 1
    else:
        other_count += 1

hearthstone_percent = (hearthstone_count / sold_games) * 100
fornite_percent = (fornite_count / sold_games) * 100
overwatch_percent = (overwatch_count / sold_games) * 100
other_percent = (other_count / sold_games) * 100
print(f"Hearthstone - {hearthstone_percent :.2f}%")
print(f"Fornite - {fornite_percent :.2f}%")
print(f"Overwatch - {overwatch_percent :.2f}%")
print(f"Others - {other_percent :.2f}%")
