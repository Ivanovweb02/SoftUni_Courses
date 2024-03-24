season = input()
kilometers_per_month = float(input())
price_per_kilometers = 0

if season == "Spring" or season == "Autumn":
    if kilometers_per_month <= 5000:
        price_per_kilometers = kilometers_per_month * 0.75
    elif kilometers_per_month <= 10_000:
        price_per_kilometers = kilometers_per_month * 0.95
elif season == "Summer":
    if kilometers_per_month <= 5000:
        price_per_kilometers = kilometers_per_month * 0.90
    elif kilometers_per_month <= 10_000:
        price_per_kilometers = kilometers_per_month * 1.10
elif season == "Winter":
    if kilometers_per_month <= 5000:
        price_per_kilometers = kilometers_per_month * 1.05
    elif kilometers_per_month <= 10_000:
        price_per_kilometers = kilometers_per_month * 1.25

if 10_000 < kilometers_per_month <= 20_000:
    price_per_kilometers = kilometers_per_month * 1.45

received_money_per_season = price_per_kilometers * 4
taxes = received_money_per_season * 0.10
tuck_driver_salary = received_money_per_season - taxes
print(f"{tuck_driver_salary :.2f}")
