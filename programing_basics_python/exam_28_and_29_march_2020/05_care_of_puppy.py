bought_dog_food = int(input())
command = input()
total_eaten_food = 0

is_food_enough = True
while command != "Adopted":
    eaten_food = int(command)
    total_eaten_food += eaten_food
    if total_eaten_food > bought_dog_food * 1000:
        is_food_enough = False

    command = input()

if is_food_enough:
    left_food = (bought_dog_food * 1000) - total_eaten_food
    print(f"Food is enough! Leftovers: {left_food} grams.")
else:
    needed_food = total_eaten_food - (bought_dog_food * 1000)
    print(f"Food is not enough. You need {needed_food} grams more.")
