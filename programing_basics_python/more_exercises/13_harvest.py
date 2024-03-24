import math

vineyard = int(input())
grapes_per_square_meter = float(input())
needed_liters_wine = int(input())
numbers_of_workers = int(input())

wine_make = vineyard * 0.40
grapes_in_kilograms = grapes_per_square_meter * 1 * wine_make
liter_wine = grapes_in_kilograms / 2.5

if liter_wine < needed_liters_wine:
    needed_wine = math.floor(needed_liters_wine - liter_wine)
    print(f"It will be a tough winter! More {int(needed_wine)} liters wine needed.")

else:
    total_wine = math.floor(liter_wine)
    left_wine = math.ceil(liter_wine - needed_liters_wine)
    wine_per_person = math.ceil(left_wine / numbers_of_workers)
    print(f"Good harvest this year! Total wine: {int(liter_wine)} liters.")
    print(f"{left_wine} liters left -> {wine_per_person} liters per person.")
