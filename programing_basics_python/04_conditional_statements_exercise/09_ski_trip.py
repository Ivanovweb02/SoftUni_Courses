days = int(input())
type_of_accommodation = input()
evaluation = input()

discount = 0
nights = days - 1
price = 0

if type_of_accommodation == "room for one person":
    price = 18.00 * nights
    discount = 0
elif type_of_accommodation == "apartment":
    price = 25.00 * nights
    if days < 10:
        discount = price * 0.30
    elif days <= 15:
        discount = price * 0.35
    else:
        discount = price * 0.50
elif type_of_accommodation == "president apartment":
    price = 35.00 * nights
    if days < 10:
        discount = price * 0.10
    elif days <= 15:
        discount = price * 0.15
    else:
        discount = price * 0.20

final_price = price - discount

if evaluation == "positive":
    tip = final_price * 0.25
    final_price += tip
    print(f"{final_price:.2f}")
else:
    price_reduction = final_price * 0.10
    final_price -= price_reduction
    print(f"{final_price:.2f}")
