import math

price_of_tennis_rocket = float(input())
count_of_rackets = int(input())
count_of_shoes_pairs = int(input())

price_of_shoes = price_of_tennis_rocket / 6
total_price = (price_of_shoes * count_of_shoes_pairs) + (price_of_tennis_rocket * count_of_rackets)
total_price += total_price * 0.20

paid_by_djokovic = math.floor(total_price / 8)
paid_by_sponsors = math.ceil(total_price * 7/8)

print(f"Price to be paid by Djokovic {paid_by_djokovic}")
print(f"Price to be paid by sponsors {paid_by_sponsors}")
