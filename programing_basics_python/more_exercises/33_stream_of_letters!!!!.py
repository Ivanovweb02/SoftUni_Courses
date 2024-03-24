import string

command = input()
counter_per_c = 0
counter_per_o = 0
counter_per_n = 0
word = ''
sentences = ''
is_letter_included = False
while command != "End":
    symbol = command
    if symbol in string.ascii_letters:
        if symbol == 'c' and counter_per_c == 0:
            counter_per_c += 1

        elif symbol == 'o' and counter_per_o == 0:
            counter_per_o += 1

        elif symbol == 'n' and counter_per_n == 0:
            counter_per_n += 1

        else:
            word += symbol

        if counter_per_c == 1 and counter_per_o == 1 and counter_per_n == 1:
            word += " "
            sentences += word
            counter_per_c = 0
            counter_per_o = 0
            counter_per_n = 0
            word = ""
    else:
        command = input()
        continue
    command = input()
print(sentences)
