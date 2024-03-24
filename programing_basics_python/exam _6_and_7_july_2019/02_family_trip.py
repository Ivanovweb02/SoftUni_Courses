budget = float(input())
nights_count = int(input())
night_price = float(input())
percent_extra_expense = int(input())

if nights_count > 7:
    night_price -= night_price * 0.05

total_price = night_price * nights_count + (percent_extra_expense / 100) * budget

if budget >= total_price:
    left_amount = budget - total_price
    print(f"Ivanovi will be left with {left_amount :.2f} leva after vacation.")
else:
    needed_money = total_price - budget
    print(f"{needed_money :.2f} leva needed.")
