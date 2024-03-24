days = int(input())
hours = int(input())
total_parking_fee = 0

for current_day in range(1, days + 1):
    parking_fee = 0
    for current_hour in range(1, hours + 1):
        if current_day % 2 == 0 and current_hour % 2 != 0:
            parking_fee += 2.50
        elif current_day % 2 != 0 and current_hour % 2 == 0:
            parking_fee += 1.25
        else:
            parking_fee += 1
    total_parking_fee += parking_fee
    print(f"Day: {current_day} - {parking_fee :.2f} leva")

print(f"Total: {total_parking_fee :.2f} leva")
