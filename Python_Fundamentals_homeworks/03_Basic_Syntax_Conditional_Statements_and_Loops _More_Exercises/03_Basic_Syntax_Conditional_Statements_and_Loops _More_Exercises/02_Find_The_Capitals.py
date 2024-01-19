text = input()
list_of_capital = []

for index in range(len(text)):
    if text[index].isupper():
        list_of_capital.append(index)

print(list_of_capital)
