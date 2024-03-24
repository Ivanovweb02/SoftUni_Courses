egg_size = input()
egg_color = input()
count_of_lots = int(input())

egg_price = 0

if egg_size == "Large":
    if egg_color == "Red":
        egg_price = 16
    elif egg_color == "Green":
        egg_price = 12
    elif egg_color == "Yellow":
        egg_price = 9
elif egg_size == "Medium":
    if egg_color == "Red":
        egg_price = 13
    elif egg_color == "Green":
        egg_price = 9
    elif egg_color == "Yellow":
        egg_price = 7
elif egg_size == "Small":
    if egg_color == "Red":
        egg_price = 9
    elif egg_color == "Green":
        egg_price = 8
    elif egg_color == "Yellow":
        egg_price = 5

total_price = egg_price * count_of_lots
total_price -= total_price * 0.35

print(f"{total_price :.2f} leva.")
