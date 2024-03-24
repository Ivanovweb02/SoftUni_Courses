# •	Пъзел - 2.60 лв.
# •	Говореща кукла - 3 лв.
# •	Плюшено мече - 4.10 лв.
# •	Миньон - 8.20 лв.
# •	Камионче - 2 лв.

vacation_cost = float(input())
puzzle_count = int(input())
talking_doll_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

money_earned = puzzle_count * 2.60 \
               + talking_doll_count * 3 \
               + teddy_bears_count * 4.10 \
               + minions_count * 8.20 \
               + trucks_count * 2

total_toys = puzzle_count + talking_doll_count + teddy_bears_count + minions_count + trucks_count

if total_toys >= 50:
    discount = money_earned * 0.25
    money_earned -= discount

rent_cost = money_earned * 0.10
money_earned -= rent_cost

if money_earned >= vacation_cost:
    left_money = money_earned - vacation_cost
    print(f"Yes! {left_money:.2f} lv left.")

else:
    not_enough_money = vacation_cost - money_earned
    print(f"Not enough money! {not_enough_money:.2f} lv needed.")
