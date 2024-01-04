def list_of_strings(first_char: str, second_char: str) -> str:
    list_of_new_strings = []
    for current_string in range(ord(first_char) + 1, ord(second_char)):
        list_of_new_strings.append(chr(current_string))
    result = " ".join(list_of_new_strings)
    return result


first_character = input()
second_character = input()
print(list_of_strings(first_character, second_character))
