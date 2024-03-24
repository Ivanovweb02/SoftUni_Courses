budget = float(input())
season = input()    # "summer" or "winter".

vacation_place = ""
type_of_vacation = ""
vacation_cost = 0

if budget <= 100:
    vacation_place = "Bulgaria"
    if season == "summer":
        vacation_cost = budget * 0.30
    elif season == "winter":
        vacation_cost = budget * 0.70
elif budget <= 1000:
    vacation_place = "Balkans"
    if season == "summer":
        vacation_cost = budget * 0.40
    elif season == "winter":
        vacation_cost = budget * 0.80
else:
    vacation_place = "Europe"
    vacation_cost = budget * 0.90

if vacation_place == "Europe" or season == "winter":
    type_of_vacation = "Hotel"
elif season == "summer":
    type_of_vacation = "Camp"

print(f"Somewhere in {vacation_place}")
print(f"{type_of_vacation} - {vacation_cost:.2f}")
