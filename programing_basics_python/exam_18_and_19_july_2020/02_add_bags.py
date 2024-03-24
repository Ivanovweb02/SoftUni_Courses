luggage_price_over_20_kg = float(input())
luggage_kilograms = float(input())
days_to_travel = int(input())
luggage_count = int(input())

luggage_price = 0

if luggage_kilograms < 10:
    luggage_price = luggage_price_over_20_kg * 0.20
elif 10 <= luggage_kilograms <= 20:
    luggage_price = luggage_price_over_20_kg * 0.50
else:
    luggage_price = luggage_price_over_20_kg

if days_to_travel < 7:
    luggage_price += luggage_price * 0.40
elif 7 <= days_to_travel <= 30:
    luggage_price += luggage_price * 0.15
else:
    luggage_price += luggage_price * 0.10

total_price = luggage_count * luggage_price
print(f"The total price of bags is: {total_price :.2f} lv.")
