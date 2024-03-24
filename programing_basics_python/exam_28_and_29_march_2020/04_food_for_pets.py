days = int(input())
quantity_of_food = float(input())
cookies = 0
dog_food = 0
cat_food = 0
total_eaten_food = 0

for current_day in range(1, days + 1):
    eaten_dog_food = int(input())
    eaten_cat_food = int(input())
    total_eaten_food += eaten_dog_food + eaten_cat_food
    dog_food += eaten_dog_food
    cat_food += eaten_cat_food
    if current_day % 3 == 0:
        cookies += (eaten_cat_food + eaten_dog_food) * 0.10


percent_total_food = (total_eaten_food / quantity_of_food) * 100
percent_dog_food = (dog_food / total_eaten_food) * 100
percent_cat_food = (cat_food / total_eaten_food) * 100
print(f"Total eaten biscuits: {round(cookies)}gr.")
print(f"{percent_total_food :.2f}% of the food has been eaten.")
print(f"{percent_dog_food :.2f}% eaten from the dog.")
print(f"{percent_cat_food :.2f}% eaten from the cat.")
