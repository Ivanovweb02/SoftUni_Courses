import re

names = input()
regex = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
marches = re.findall(regex, names)
print(' '.join(marches))
