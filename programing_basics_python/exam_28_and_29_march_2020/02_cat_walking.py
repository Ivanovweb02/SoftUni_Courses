minutes_of_walking = int(input())
count_of_walks = int(input())
calories_intake = int(input())

burned_calories = minutes_of_walking * count_of_walks * 5

if burned_calories >= calories_intake / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")
