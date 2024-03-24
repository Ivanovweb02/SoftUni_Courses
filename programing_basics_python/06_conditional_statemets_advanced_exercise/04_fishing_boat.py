budget = int(input())
season = input()
number_of_fishmen = int(input())

rent_price = 0
discount = 0

if season == "Spring":
    rent_price = 3000
elif season == "Summer" or season == "Autumn":
    rent_price = 4200
elif season == "Winter":
    rent_price = 2600

if number_of_fishmen <= 6:
    discount = rent_price * 0.10
elif number_of_fishmen <= 11:
    discount = rent_price * 0.15
elif number_of_fishmen >= 12:
    discount = rent_price * 0.25

extra_discount = 0

total_cost = (rent_price - discount) - extra_discount

if number_of_fishmen % 2 == 0 and not season == "Autumn":
    extra_discount = total_cost * 0.05
    total_cost -= extra_discount


if budget >= total_cost:
    left_money = budget - total_cost
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    needed_money = total_cost - budget
    print(f"Not enough money! You need {needed_money:.2f} leva.")
