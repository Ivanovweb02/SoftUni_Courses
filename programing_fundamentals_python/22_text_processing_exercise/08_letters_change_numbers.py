sequence = input().split()
final_results = []
for text in sequence:
    result = 0
    number = ''
    for i in range(len(text)):
        if text[i].isdigit():
            number += str(text[i])
    number = int(number)
    for i in range(len(text)):
        if text[i].isdigit() and text[i - 1].isalpha():
            start_word = text[i - 1]
            if start_word.isupper():
                num = ord(start_word) - 64
                result = number / num
            elif start_word.islower():
                num = ord(start_word) - 96
                result = number * num
        if text[i].isdigit() and text[i + 1].isalpha():
            end_word = text[i + 1]
            if end_word.isupper():
                num = ord(end_word) - 64
                result -= num
            elif end_word.islower():
                num = ord(end_word) - 96
                result += num
    final_results.append(result)

final_results = sum(final_results)
print(f"{final_results :.2f}")
