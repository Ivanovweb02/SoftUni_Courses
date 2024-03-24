text = input()
point = 0

for character in text:
    if character == "a":
        point += 1
    elif character == "e":
        point += 2
    elif character == "i":
        point += 3
    elif character == "o":
        point += 4
    elif character == "u":
        point += 5
print(point)
