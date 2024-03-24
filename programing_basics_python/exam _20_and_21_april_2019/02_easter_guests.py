import math

count_guest = int(input())
budget = int(input())

count_easter_bread = math.ceil(count_guest / 3)
count_eggs = count_guest * 2

easter_bread_price = count_easter_bread * 4
eggs_price = count_eggs * 0.45

total_price = easter_bread_price + eggs_price

if budget >= total_price:
    left_money = budget - total_price
    print(f"Lyubo bought {count_easter_bread} Easter bread and {count_eggs} eggs.")
    print(f"He has {left_money :.2f} lv. left.")
else:
    needed_money = total_price - budget
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {needed_money :.2f} lv. more.")
