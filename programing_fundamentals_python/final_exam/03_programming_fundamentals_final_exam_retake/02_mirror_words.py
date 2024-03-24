import re

some_string = input()
pattern = r'(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'
matches = re.finditer(pattern, some_string)
count_of_pairs = 0
is_mirror_word = False
list_of_mirror_words = []
for match in matches:
    count_of_pairs += 1
    if match.group(2) == match.group(3)[::-1] \
            or match.group(2)[::-1] == match.group(3):
        is_mirror_word = True
        list_of_mirror_words.append(match.group(2))
        list_of_mirror_words.append(match.group(3))
if count_of_pairs == 0:
    print("No word pairs found!")
else:
    print(f"{count_of_pairs} word pairs found!")

if is_mirror_word:
    print("The mirror words are:")
    for index in range(0, len(list_of_mirror_words), 2):
        if index == len(list_of_mirror_words) - 2:
            print(f"{list_of_mirror_words[index]} <=> {list_of_mirror_words[index + 1]}")
            break
        print(f"{list_of_mirror_words[index]} <=> {list_of_mirror_words[index + 1]}", end=', ')
else:
    print("No mirror words!")

