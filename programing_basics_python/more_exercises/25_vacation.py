budget = float(input())
season = input()
accommodation = ""
location = ""
vacation_cost = 0

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        vacation_cost = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        vacation_cost = budget * 0.45

elif budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        vacation_cost = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        vacation_cost = budget * 0.60

else:
    accommodation = "Hotel"
    vacation_cost = budget * 0.90
    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"

print(f"{location} - {accommodation} - {vacation_cost :.2f}")
