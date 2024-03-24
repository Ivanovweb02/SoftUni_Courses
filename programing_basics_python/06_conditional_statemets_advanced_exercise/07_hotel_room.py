month = input()
nights = int(input())

Apartment = 0
Studio = 0
price_per_night = 0
discount_studio = 0
discount_apartment = 0

if month == "May" or month == "October":
    Studio = 50 * nights
    Apartment = 65 * nights
elif month == "June" or month == "September":
    Studio = 75.20 * nights
    Apartment = 68.70 * nights

elif month == "July" or month == "August":
    Studio = 76 * nights
    Apartment = 77 * nights

if 14 >= nights > 7 and (month == "May" or month == "October"):
    discount_studio = Studio * 0.05
elif nights > 14 and (month == "May" or month == "October"):
    discount_studio = Studio * 0.30
elif nights > 14 and (month == "June" or month == "September"):
    discount_studio = Studio * 0.20

if nights > 14:
    discount_apartment = Apartment * 0.10

final_price_for_studio = Studio - discount_studio
final_price_for_apartment = Apartment - discount_apartment

print(f"Apartment: {final_price_for_apartment:.2f} lv.")
print(f"Studio: {final_price_for_studio:.2f} lv.")
