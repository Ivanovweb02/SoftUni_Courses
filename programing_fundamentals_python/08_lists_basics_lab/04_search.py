number = int(input())
special_word = input()
list_of_word = []
list_of_special_word = []
for _ in range(number):
    current_word = input()
    list_of_word.append(current_word)
    if special_word in current_word:
        list_of_special_word.append(current_word)
print(list_of_word)
print(list_of_special_word)
