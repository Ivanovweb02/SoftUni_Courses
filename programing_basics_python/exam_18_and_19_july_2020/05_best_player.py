command = input()
best_player = ""
max_goals = 0

is_he_made_hat_trick = False
while command != "END":
    player_name = command
    count_of_goals = int(input())
    if count_of_goals > max_goals:
        max_goals = count_of_goals
        best_player = player_name
    if count_of_goals >= 3:
        is_he_made_hat_trick = True
    if count_of_goals >= 10:
        break
    command = input()

print(f"{best_player} is the best player!")
if is_he_made_hat_trick:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")
