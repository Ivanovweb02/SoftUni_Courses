hall_rent = float(input())

cake_price = hall_rent * 0.20
drinks = cake_price * (1 - 0.45)
animator = hall_rent / 3

budget_needed = hall_rent + cake_price + drinks + animator
print(f"{budget_needed :.1f}")
