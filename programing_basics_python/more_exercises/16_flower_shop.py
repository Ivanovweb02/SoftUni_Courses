import math

count_of_magnolias = int(input())
count_of_hyacinths = int(input())
count_of_roses = int(input())
count_of_cacti = int(input())
price_of_gift = float(input())

total_amount = count_of_magnolias * 3.25 \
               + count_of_hyacinths * 4 \
               + count_of_roses * 3.50 \
               + count_of_cacti * 8

total_amount -= total_amount * 0.05    # taxes

if total_amount >= price_of_gift:
    left_amount = math.floor(total_amount - price_of_gift)
    print(f"She is left with {int(left_amount)} leva.")
else:
    needed_money = math.ceil(price_of_gift - total_amount)
    print(f"She will have to borrow {int(needed_money)} leva.")
