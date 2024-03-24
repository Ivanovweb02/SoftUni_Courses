budget = float(input())
actors_count = int(input())
clothing_price = float(input())

decor_price = budget * 0.10
if actors_count >= 150:
    clothing_price -= clothing_price * 0.10

total_price = clothing_price * actors_count + decor_price
if budget >= total_price:
    left_money = budget - total_price
    print(f"Action!")
    print(f"Wingard starts filming with {left_money :.2f} leva left.")
else:
    needed_money = total_price - budget
    print("Not enough money!")
    print(f"Wingard needs {needed_money :.2f} leva more.")
