text = input()

count = 0
word_1 = 'sand'
word_2 = 'water'
word_3 = 'fish'
word_4 = 'sun'

if word_1 in text.lower():
    count += text.lower().count(word_1)
if word_2 in text.lower():
    count += text.lower().count(word_2)
if word_3 in text.lower():
    count += text.lower().count(word_3)
if word_4 in text.lower():
    count += text.lower().count(word_4)
print(count)
