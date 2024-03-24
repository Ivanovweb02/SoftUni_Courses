import re

some_string = input()
food_list = []
total_calories = 0
pattern = r"(#|\|)([A-Za-z\s]+)\1(\d{2,2}/\d{2,2}/\d{2,2})\1(\d{1,5})\1"

for match in (re.finditer(pattern, some_string)):
    food_list.append([match.group(2), match.group(3), match.group(4)])
    total_calories += int(match.group(4))


food_duration = total_calories // 2000
print(f"You have food to last you for: {food_duration} days!")
for match in food_list:
    print(f"Item: {match[0]}, Best before: {match[1]}, Nutrition: {match[2]}")
