import re

lines = int(input())
pattern_name = r'@([A-Za-z]+)\|'
pattern_age = r'#(\d+)\*'
for _ in range(lines):

    some_text = input()
    name_match = re.search(pattern_name, some_text)
    age_match = re.search(pattern_age, some_text)
    if name_match and age_match:
        name = name_match.group(1)
        age = age_match.group(1)
        print(f"{name} is {age} years old.")
