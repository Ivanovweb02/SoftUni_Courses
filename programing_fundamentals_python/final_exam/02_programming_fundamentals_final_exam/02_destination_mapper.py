import re

some_string = input()
travel_list = []
travel_points = 0
pattern = r"(=|/)([A-Z]{1}[A-Za-z]{2,})\1"
matches = re.findall(pattern, some_string)

for match in matches:
    destination = match[1]
    travel_list.append(destination)
for destination in travel_list:
    point = len(destination)
    travel_points += point

print(f"Destinations: {', '.join(travel_list)}")
print(f"Travel Points: {travel_points}")
