strawberries_price = float(input())
quantity_bananas = float(input())
quantity_oranges = float(input())
quantity_raspberries = float(input())
quantity_strawberries = float(input())

raspberries_price = strawberries_price * 0.50
oranges_price = raspberries_price * (1 - 0.40)
bananas_price = raspberries_price * (1 - 0.80)

total_price = strawberries_price * quantity_strawberries \
              + bananas_price * quantity_bananas \
              + oranges_price * quantity_oranges \
              + raspberries_price * quantity_raspberries
print(f"{total_price :.2f}")
