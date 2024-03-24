degree = int(input())
time_of_the_day = input()

Outfit = ""
Shoes = ""

if time_of_the_day == "Morning":
    if 10 <= degree <= 18:
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
    elif degree <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    else:
        Outfit = "T-Shirt"
        Shoes = "Sandals"

elif time_of_the_day == "Afternoon":
    if 10 <= degree <= 18:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif degree <= 24:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    else:
        Outfit = "Swim Suit"
        Shoes = "Barefoot"

elif time_of_the_day == "Evening":
    Outfit = "Shirt"
    Shoes = "Moccasins"

print(f"It's {degree} degrees, get your {Outfit} and {Shoes}.")
