list_of_characters = input().split(', ')

ascii_values = {char: ord(char) for char in list_of_characters}
print(ascii_values)
