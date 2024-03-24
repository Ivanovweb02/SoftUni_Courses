budget = float(input())
destination = input()
season = input()
days = int(input())

price_per_day = 0

if season == "Winter":
    if destination == "Dubai":
        price_per_day = 45_000
    elif destination == "Sofia":
        price_per_day = 17_000
    elif destination == "London":
        price_per_day = 24_000
elif season == "Summer":
    if destination == "Dubai":
        price_per_day = 40_000
    elif destination == "Sofia":
        price_per_day = 12_500
    elif destination == "London":
        price_per_day = 20_250

total_price = price_per_day * days
if destination == "Dubai":
    total_price -= total_price * 0.30
if destination == "Sofia":
    total_price += total_price * 0.25

if budget >= total_price:
    left_money = budget - total_price
    print(f"The budget for the movie is enough! We have {left_money :.2f} leva left!")
else:
    needed_money = total_price - budget
    print(f"The director needs {needed_money :.2f} leva more!")
