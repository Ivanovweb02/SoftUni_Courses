vegetable_price_in_kilograms = float(input())
fruit_price_in_kilograms = float(input())
vegetable_count_in_kilogram = int(input())
fruit_count_in_kilogram = int(input())

total_income = vegetable_price_in_kilograms * vegetable_count_in_kilogram \
               + fruit_price_in_kilograms * fruit_count_in_kilogram   # total income in leva

total_income /= 1.94    # in euro
print(f"{total_income:.2f}")
