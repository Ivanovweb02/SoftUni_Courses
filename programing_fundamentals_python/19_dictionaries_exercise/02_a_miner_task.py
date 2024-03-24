dictionary = {}
list_of_minerals = []

while True:
    mineral = input()
    if mineral == 'stop':
        break
    list_of_minerals.append(mineral)

for index in range(0, len(list_of_minerals), 2):
    mineral = list_of_minerals[index]
    quantity = int(list_of_minerals[index + 1])
    if mineral not in dictionary:
        dictionary[mineral] = quantity
    else:
        dictionary[mineral] += quantity

for (mineral, quantity) in dictionary.items():
    print(f"{mineral} -> {quantity}")
