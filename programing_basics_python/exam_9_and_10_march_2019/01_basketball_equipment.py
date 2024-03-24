annual_fee = int(input())

basketball_shoes = annual_fee * (1 - 0.40)
basketball_outfit = basketball_shoes * (1 - 0.20)
basket_ball = basketball_outfit / 4
basketball_accessories = basket_ball / 5

total_price = annual_fee \
              + basketball_shoes \
              + basketball_outfit \
              + basket_ball \
              + basketball_accessories

print(f"{total_price :.2f}")
