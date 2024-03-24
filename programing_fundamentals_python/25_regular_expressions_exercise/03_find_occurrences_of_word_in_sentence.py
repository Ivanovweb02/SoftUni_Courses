import re

some_string = input()
searched_word = input()
pattern = fr'(?i)\b{searched_word}\b'
matches = re.findall(pattern, some_string)
print(len(matches))
