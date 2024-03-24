budget = float(input())
season = input()
vehicle_class = ""
vehicle_type = ""
car_price = 0

if budget <= 100:
    vehicle_class = "Economy class"
    if season == "Summer":
        vehicle_type = "Cabrio"
        car_price = budget * 0.35
    elif season == "Winter":
        vehicle_type = "Jeep"
        car_price = budget * 0.65

elif budget <= 500:
    vehicle_class = "Compact class"
    if season == "Summer":
        vehicle_type = "Cabrio"
        car_price = budget * 0.45
    elif season == "Winter":
        vehicle_type = "Jeep"
        car_price = budget * 0.80

else:
    vehicle_class = "Luxury class"
    vehicle_type = "Jeep"
    car_price = budget * 0.90

print(vehicle_class)
print(f"{vehicle_type} - {car_price :.2f}")
