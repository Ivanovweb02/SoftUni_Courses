painted_eggs = int(input())
red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
max_egg = 0
color = ""
for _ in range(1, painted_eggs + 1):
    egg_color = input()    # "red", "orange", "blue", "green"
    if egg_color == "red":
        red_eggs += 1
    elif egg_color == "orange":
        orange_eggs += 1
    elif egg_color == "blue":
        blue_eggs += 1
    elif egg_color == "green":
        green_eggs += 1

if red_eggs > orange_eggs and red_eggs > blue_eggs and red_eggs > green_eggs:
    max_egg = red_eggs
    color = "red"
elif orange_eggs > red_eggs and orange_eggs > blue_eggs and orange_eggs > green_eggs:
    max_egg = orange_eggs
    color = "orange"
elif blue_eggs > red_eggs and blue_eggs > orange_eggs and blue_eggs > green_eggs:
    max_egg = blue_eggs
    color = "blue"
elif green_eggs > red_eggs and green_eggs > orange_eggs and green_eggs > blue_eggs:
    max_egg = green_eggs
    color = "green"

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {max_egg} -> {color}")
