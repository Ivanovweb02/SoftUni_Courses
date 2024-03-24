import math

people_count = int(input())
entrance_fee = float(input())
lounger_price = float(input())
umbrella_price = float(input())

total_entrance_fee = entrance_fee * people_count
total_umbrella_price = umbrella_price * math.ceil(people_count / 2)
total_lounger_price = lounger_price * math.ceil(people_count * 0.75)

total_price = total_lounger_price + total_umbrella_price + total_entrance_fee
print(f"{total_price :.2f} lv.")
