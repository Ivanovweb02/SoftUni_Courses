budget = float(input())
needed_fuel = float(input())
day_of_the_weekend = input()

discount = 0
fuel_cost = needed_fuel * 2.10
tour_guid_price = 100
total_price = fuel_cost + tour_guid_price

if day_of_the_weekend == "Saturday":
    discount = total_price * 0.10
elif day_of_the_weekend == "Sunday":
    discount = total_price * 0.20

total_price -= discount
if budget >= total_price:
    left_money = budget - total_price
    print(f"Safari time! Money left: {left_money :.2f} lv. ")
else:
    needed_money = total_price - budget
    print(f"Not enough money! Money needed: {needed_money :.2f} lv.")
