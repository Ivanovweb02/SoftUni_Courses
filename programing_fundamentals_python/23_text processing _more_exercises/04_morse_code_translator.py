morse_code_dict = {'A': '.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def morse_translate(some_char):
    for letter in morse_code_dict:
        if some_char == morse_code_dict[letter]:
            some_char = letter
            return some_char


morse_message = input()
words_in_morse = morse_message.split(' | ')
translate_message = ''

for word in words_in_morse:
    chars_in_morse = word.split()
    translate_word = ''
    for curr_char in chars_in_morse:
        translate_word += morse_translate(curr_char)
    if word != words_in_morse[-1]:
        translate_message += translate_word + " "
    else:
        translate_message += translate_word

print(translate_message)