import re

some_string = input()
pattern = r'(:{2}|\*{2})([A-Z][a-z]{2,})\1'
matches = re.findall(pattern, some_string)
emoji_count = 0
cool_threshold = 1
for char in some_string:
    if char.isdigit():
        cool_threshold *= int(char)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")

for match in matches:
    emoji = match[1]
    emoji_coolness = 0
    for char in emoji:
        if char.isalpha():
            emoji_coolness += ord(char)
    if emoji_coolness >= cool_threshold:
        print(f"{match[0]}{emoji}{match[0]}")
