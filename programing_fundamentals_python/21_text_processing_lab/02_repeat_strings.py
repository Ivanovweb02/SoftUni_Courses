strings = input().split()
concatenated_string = ''
for string in strings:
    for _ in range(len(string)):
        concatenated_string += string
print(concatenated_string)
