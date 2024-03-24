text = input()
symbol = ":"

for i in range(len(text)):
    if text[i] == symbol:
        print(text[i] + text[i + 1])
