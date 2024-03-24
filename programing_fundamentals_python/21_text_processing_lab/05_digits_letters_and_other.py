symbols = input()
digit = ''
string = ''
other = ''

for char in symbols:
    if char.isdigit():
        digit += char
    elif char.isalpha():
        string += char
    else:
        other += char

print(digit)
print(string)
print(other)
