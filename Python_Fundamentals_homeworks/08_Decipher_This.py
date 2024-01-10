secret_words = input().split()
deciphered_message = []

for word in secret_words:
    message = []
    digit_to_str = ''
    other_characters = ''
    for character in word:
        if character.isdigit():
            digit_to_str += character
        else:
            other_characters += character

    message += (chr(int(digit_to_str))) + other_characters
    message[1], message[-1] = message[-1], message[1]
    message_to_word = ''.join(message)
    deciphered_message.append(message_to_word)

result = ' '.join(deciphered_message)
print(result)
