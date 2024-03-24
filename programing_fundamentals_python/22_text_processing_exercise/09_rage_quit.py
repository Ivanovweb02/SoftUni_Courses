some_string = input().upper()
unique_symbols = ''
current_string = ''
repetition = ''

for index in range(len(some_string)):
    if not some_string[index].isnumeric():
        current_string += some_string[index]
    else:
        for count in range(index, len(some_string)):
            if some_string[count].isnumeric():
                repetition += some_string[count]
            else:
                break
        unique_symbols += current_string * int(repetition)
        current_string = ''
        repetition = ''

print(f"Unique symbols used: {len(set(unique_symbols))}")
print(unique_symbols)
