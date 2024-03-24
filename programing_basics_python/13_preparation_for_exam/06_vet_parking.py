count_of_days = int(input())
count_of_hours = int(input())
total_amount = 0

for current_day in range(1, count_of_days + 1):
    fee_per_day = 0
    for current_hours in range(1, count_of_hours + 1):
        if current_day % 2 == 0 and current_hours % 2 != 0:
            fee_per_day += 2.50
        elif current_day % 2 != 0 and current_hours % 2 == 0:
            fee_per_day += 1.25
        else:
            fee_per_day += 1.00
    total_amount += fee_per_day

    print(f"Day: {current_day} - {fee_per_day :.2f} leva")

print(f"Total: {total_amount :.2f} leva")
