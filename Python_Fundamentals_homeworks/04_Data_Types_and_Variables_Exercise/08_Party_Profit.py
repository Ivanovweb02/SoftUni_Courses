import math

group_members = int(input())
days = int(input())
coins = 0

for current_days in range(1, days + 1):
    if current_days % 15 == 0:
        group_members += 5
    if current_days % 10 == 0:
        group_members -= 2
    if current_days % 3 == 0:
        coins -= 3 * group_members
    if current_days % 5 == 0:
        coins += 20 * group_members
        if current_days % 3 == 0:
            coins -= 2 * group_members
    coins += 50
    coins -= 2 * group_members
coins_per_member = int(coins / group_members)
print(f"{group_members} companions received {coins_per_member} coins each.")
