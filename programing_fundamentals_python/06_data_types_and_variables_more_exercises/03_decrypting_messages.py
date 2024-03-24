key = int(input())
number_of_lines = int(input())
decrypted_word = ''

for _ in range(number_of_lines):
    character = input()
    char_to_ascii = ord(character) + key
    decrypted_word += chr(char_to_ascii)

print(decrypted_word)
