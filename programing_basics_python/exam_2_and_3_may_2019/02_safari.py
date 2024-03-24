budget = float(input())
quantity_needed_fuel = float(input())
dey_of_weekend = input()

fuel_price = quantity_needed_fuel * 2.10
tour_guide_price = 100

total_amount = fuel_price + tour_guide_price
if dey_of_weekend == "Saturday":
    total_amount -= total_amount * 0.10
elif dey_of_weekend == "Sunday":
    total_amount -= total_amount * 0.20

if budget >= total_amount:
    left_money = budget - total_amount
    print(f"Safari time! Money left: {left_money :.2f} lv. ")
else:
    needed_money = total_amount - budget
    print(f"Not enough money! Money needed: {needed_money :.2f} lv.")
