from collections import deque

word = deque(input().split())

valid_color = ["red", "yellow", "blue", "orange", "purple", "green"]
color_request = {
    'orange': {'red', 'yellow'},
    'purple': {'red', 'blue'},
    'green': {'yellow', 'blue'}
}

result = []

while word:
    first_word = word.popleft()
    last_word = word.pop() if word else ''

    for color in ((first_word + last_word), (last_word + first_word)):
        if color in valid_color:
            result.append(color)
            break
    else:
        for el in (first_word[:-1], last_word[:-1]):
            if el:
                word.insert(len(word) // 2, el)

for color in set(color_request.keys()).intersection(result):
    if not color_request[color].issubset(result):
        result.remove(color)

print(result)
