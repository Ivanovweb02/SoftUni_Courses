from string import punctuation

with open('files//file_1.txt', 'r') as text_file:
    text = text_file.readlines()

output_file = open('files//output_1.txt', 'w')

for row in range(len(text)):
    letters, marks = 0, 0

    for symbols in text[row]:
        if symbols.isalpha():
            letters += 1

        elif symbols in punctuation:
            marks += 1

    output_file.write(f'Line {row + 1}: {text[row][:-1]} ({letters})({marks})\n')


output_file.close()
