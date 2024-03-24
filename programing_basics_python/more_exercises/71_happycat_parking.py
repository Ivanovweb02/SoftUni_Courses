days = int(input())
hours_per_day = int(input())
total_amount = 0

for current_day in range(1, days + 1):
    amount_per_day = 0
    for current_hour in range(1, hours_per_day + 1):
        if current_day % 2 == 0 and current_hour % 2 != 0:
            amount_per_day += 2.50
        elif current_hour % 2 == 0 and current_day % 2 != 0:
            amount_per_day += 1.25
        else:
            amount_per_day += 1
    total_amount += amount_per_day
    print(f'Day: {current_day} - {amount_per_day :.2f} leva')
print(f'Total: {total_amount :.2f} leva')
