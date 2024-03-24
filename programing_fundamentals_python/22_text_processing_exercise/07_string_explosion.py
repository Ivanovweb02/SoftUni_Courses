some_string = input()
explosion_range = 0
new_string = ''

for i in range(len(some_string)):
    if some_string[i] == '>':
        new_string += some_string[i]
        explosion_range += int(some_string[i + 1])
    elif some_string != '>' and explosion_range > 0:
        explosion_range -= 1
    else:
        new_string += some_string[i]

print(new_string)
