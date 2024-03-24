import math
import sys

command = input()
max_point = -sys.maxsize
strongest_word = ""
list_of_vowels = ['a','e','i','o','u','y','A','E','I','O','U','Y']

while command != "End of words":
    word = command
    word_length = len(word)
    point = 0
    for chart in word:
        ascii_value = ord(chart)
        if word[0] in list_of_vowels:
            point += ascii_value * word_length
        else:
            point += math.floor(ascii_value / word_length)
    if point > max_point:
        max_point = point
        strongest_word = word
    command = input()

print(f"The most powerful word is {strongest_word} - {max_point}")
