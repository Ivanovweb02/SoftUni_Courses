import re

some_string = input()
regex = r"\b_([A-Za-z0-9]+)\b"
matches = re.findall(regex, some_string)
print(','.join(matches))
