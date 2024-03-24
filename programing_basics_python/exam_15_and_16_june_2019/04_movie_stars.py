budget = float(input())
command = input()
total_cost = 0

is_budget_off = False

while command != "ACTION":
    actor_name = command
    name_length = len(actor_name)

    if name_length <= 15:
        reward = float(input())
    else:
        reward = budget * 0.20
    if reward > budget:
        is_budget_off = True
        break
    budget -= reward

    command = input()

if is_budget_off:
    needed_budget = reward - budget
    print(f"We need {needed_budget :.2f} leva for our actors.")
else:
    print(f"We are left with {budget :.2f} leva.")
