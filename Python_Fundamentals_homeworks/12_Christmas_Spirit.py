decoration = int(input())
remaining_days = int(input())
price_per_ornament_set = 2
price_per_tree_skirt = 5
price_per_tree_garland = 3
price_per_tree_light = 15
total_cost = 0
total_spirit = 0

for current_day in range(1, remaining_days + 1):
    if current_day % 11 == 0:
        decoration += 2
    if current_day % 2 == 0:
        total_cost += decoration * price_per_ornament_set
        total_spirit += 5
    if current_day % 3 == 0:
        total_cost += decoration * (price_per_tree_skirt + price_per_tree_garland)
        total_spirit += 10 + 3
    if current_day % 5 == 0:
        total_cost += decoration * price_per_tree_light
        total_spirit += 17
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        total_cost += price_per_tree_skirt + price_per_tree_garland + price_per_tree_light

if remaining_days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
