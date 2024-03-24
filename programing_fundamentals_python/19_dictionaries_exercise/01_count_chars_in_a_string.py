string = [char for char in input() if char != " "]
dictionary = {}

for char in string:
    if char not in dictionary.keys():
        dictionary[char] = 0
    dictionary[char] += 1

for (key, value) in dictionary.items():
    print(f"{key} -> {value}")
