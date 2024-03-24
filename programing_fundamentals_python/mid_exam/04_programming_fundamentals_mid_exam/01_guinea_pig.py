# everything is on kilograms

quantity_of_food = float(input())
quantity_of_hay = float(input())
quantity_of_cover = float(input())
guinea_weight = float(input())

days = 30
is_food_enough = True
for day in range(1, days + 1):
    eaten_food_in_kg = 300 / 1000   # per day
    if quantity_of_food < eaten_food_in_kg \
            or quantity_of_hay < (quantity_of_food * 0.05) \
            or quantity_of_cover < (guinea_weight / 3):
        is_food_enough = False
        break
    quantity_of_food -= eaten_food_in_kg
    if day % 2 == 0:

        quantity_of_hay -= quantity_of_food * 0.05
    if day % 3 == 0:

        quantity_of_cover -= guinea_weight / 3

if is_food_enough:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_of_food :.2f}, Hay: {quantity_of_hay :.2f}, "
          f"Cover: {quantity_of_cover :.2f}.")

else:
    print("Merry must go to the pet store!")
