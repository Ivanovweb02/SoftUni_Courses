import math

days = int(input())
food_left = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())
turtle_food_per_day_in_kilogram = turtle_food_per_day / 1000

consummation_per_day = dog_food_per_day + cat_food_per_day + turtle_food_per_day_in_kilogram
total_consummation = days * consummation_per_day

if food_left >= total_consummation:
    leftover_food = math.floor(food_left - total_consummation)
    print(f"{int(leftover_food)} kilos of food left.")
else:
    needed_food = math.ceil(total_consummation- food_left)
    print(f"{int(needed_food)} more kilos of food are needed.")
