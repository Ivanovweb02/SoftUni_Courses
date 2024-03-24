some_string = input()
new_string = []

for char in some_string:
    if char in new_string:
        if char != new_string[-1]:
            new_string.append(char)
    else:
        new_string.append(char)
print(''.join(new_string))
