days_of_tournament = int(input())
total_earned_money = 0
wins = 0
loses = 0

is_tournament_won = False
for _ in range(days_of_tournament):
    current_wins = 0
    current_loses = 0
    command = input()
    earned_money = 0
    while command != "Finish":
        sport = command
        result = input()
        if result == "win":
            current_wins += 1
            wins += 1
            earned_money += 20
        else:
            current_loses += 1
            loses += 1
        command = input()
    if current_wins > current_loses:
        earned_money += earned_money * 0.10
    total_earned_money += earned_money
if wins > loses:
    is_tournament_won = True
    total_earned_money += total_earned_money * 0.20

if is_tournament_won:
    print(f"You won the tournament! Total raised money: {total_earned_money :.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_earned_money :.2f}")
