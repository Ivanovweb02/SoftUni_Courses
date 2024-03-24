wanted_income = float(input())
command = input()
total_income = 0

is_amount_reached = False
while command != "Party!":
    cocktail_name = command
    cocktail_count = int(input())
    price = len(cocktail_name)
    price *= cocktail_count
    if price % 2 != 0:
        price -= price * 0.25
    total_income += price
    if total_income >= wanted_income:
        is_amount_reached = True
        break
    command = input()

if is_amount_reached:
    print("Target acquired.")
else:
    needed_amount = wanted_income - total_income
    print(f"We need {needed_amount :.2f} leva more.")

print(f"Club income - {total_income :.2f} leva.")
