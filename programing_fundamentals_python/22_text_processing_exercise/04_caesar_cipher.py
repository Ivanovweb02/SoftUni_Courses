text = input()
encrypted_text = ''

for char in text:
    ascii_char = ord(char)
    ascii_char += 3
    encrypted_char = chr(ascii_char)
    encrypted_text += encrypted_char

print(encrypted_text)
